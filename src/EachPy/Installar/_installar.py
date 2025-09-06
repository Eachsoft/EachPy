"""
Projucer project generation. Use python to generate .jucer files that can
then be opened with Projucer and re-saved or re-save the generated projects from
command line using Projucer cli.
"""
from collections import OrderedDict
import sys
import uuid
import string
import random
import os
import subprocess
import glob
import codecs
from filecmp import dircmp
import shutil
import html
import time
from pathlib import Path

import EachPy.Io

class InstallarNode:
  def __init__(self):
    super(InstallarNode,self).__init__()
    self.attrs = OrderedDict()

  def __getitem__(self, index):
        # Access the element at the given index in the _data list
        return self.attrs[index]

  def __setitem__(self, index, value):
        # Set the element at the given index in the _data list
        self.attrs[index] = value

  def __len__(self):
        # Return the length of the _data list
        return len(self.attrs)


class Component(InstallarNode):
  def __init__(self,name,path,dest,required=False):
    super(Component,self).__init__()
    self["NAME"] = name
    self["PATH"] = path
    self["DEST"] = dest
    self["REQUIRED"] = required

class Project(InstallarNode):
  def __init__(self,ctx):
    super(Project,self).__init__()
    self.Components = []
    self["PACKAGE_NAME"] = "Installer"
    self["PACKAGE_VERSION"] = "1.0.0"
    self["PACKAGE_VENDOR"] = "John Somebody"
    self["PACKAGE_DESCRIPTION"] = "Installer application"
    self["PACKAGE_LICENSE"] = None
    self["PACKAGE_ICON"] =None
    self["PACKAGE_README"] =None
    self["PACKAGE_INSTALL_SCRIPTS"]=None
    self.Context = ctx

  
  def NewComponent(self,name,path,dest,required=False):
    c = Component(name,path,dest,required)
    self.Components.append(c)
    return c


  def PutComponents(self,hdr):
      hdr.PutLnIdn("# Specify installation locations")
      comps = ""
      first_comp = ""
      for c in self.Components:
        if first_comp == "":
          first_comp = c["NAME"]
        if os.path.isfile(c["PATH"]):
          sk = "FILES"
          sp = ""
        else: 
          sk = "DIRECTORY"    
          sp = "USE_SOURCE_PERMISSIONS"

        hdr.PutLnIdn("install("+sk+" \"" + c["PATH"] + "\"" 
                     " DESTINATION \"" + c["DEST"] + "\"" +
                     " EXCLUDE_FROM_ALL "+sp+" COMPONENT "+c["NAME"]+")")
        if comps != "": comps += " "              
        comps += c["NAME"]              
        is_req = c["REQUIRED"]
        if is_req: is_req = "TRUE"
        else: is_req = "FALSE"
        hdr.PutLnIdn("set(CPACK_COMPONENT_"+c["NAME"]+"_REQUIRED "+is_req+")")
      hdr.PutLnIdn("set(CPACK_MONOLITHIC_INSTALL OFF)")
      hdr.PutLnIdn("set(CPACK_COMPONENTS_ALL "+comps+")")
      return first_comp  

  def PutPreScript(self,hdr,first_comp):
    install_scripts = self["PACKAGE_INSTALL_SCRIPTS"]
    if install_scripts != None:
      #hdr.PutLnIdn("cpack_add_component(pre_script  DISPLAY_NAME \"Pre-installation Script\"  HIDDEN  REQUIRED)")
      # Define a "hidden" component for your pre-install script.
      # This component doesn't install files, but serves as a way to attach a script.
      hdr.PutLnIdn("install(CODE \"message(STATUS \\\"Installing pre_script\\\")\" COMPONENT pre_script)")

      # Set the pre-installation script for the 'pre_script' component.
      # The component name must be uppercase here.
      hdr.PutLnIdn("set(CPACK_PREFLIGHT_PRE_SCRIPT \""+install_scripts+"\")")

      # Set the properties for the components
      hdr.PutLnIdn("set(CPACK_COMPONENT_PRE_SCRIPT_DISPLAY_NAME \"Pre-installation Script\")")
      hdr.PutLnIdn("set(CPACK_COMPONENT_PRE_SCRIPT_HIDDEN TRUE)")
      hdr.PutLnIdn("set(CPACK_COMPONENT_PRE_SCRIPT_REQUIRED TRUE)")      

      # Set the pre-installation script for the 'pre_script' component
      #hdr.PutLnIdn("set(CPACK_PREFLIGHT_PRE_SCRIPT \""+install_scripts+"\")")

      # Tell CPack that the main application component depends on the script component.
      # This ensures the script's package is installed *before* the main application.
      hdr.PutLnIdn("set(CPACK_COMPONENT_DEPENDS \""+first_comp+":pre_script\")")

      if False:
        #hdr.PutLnIdn("set(CPACK_PRE_BUILD_SCRIPTS \""+install_scripts+"\")")
        hdr.PutLnIdn("install(CODE \"message(STATUS \"Installing pre_script\")\" COMPONENT pre_script)")

        # Set the pre-installation script for the 'pre_script' component
        hdr.PutLnIdn("set(CPACK_PREFLIGHT_PRE_SCRIPT \""+install_scripts+"\")")

        # The order matters. Set dependencies so the script runs first.
        # Make the main app component depend on the script component.
        hdr.PutLnIdn("set_property(INSTALL_COMPONENT "+first_comp+" PROPERTY DEPENDS pre_script)")
      pass


  def Generate(self):
    ctx = self.Context
    working_dir = ctx["WORKING_DIR"]
    os.makedirs(working_dir, exist_ok=True)     
    fn = working_dir + "/CMakeLists.txt"
    hdr = EachPy.Io.FileWriter(fn)
    print("Generating CMakeLists.txt: " + fn)
    
    hdr.PutLnIdn("cmake_minimum_required(VERSION 3.20)")
    hdr.PutLnIdn("# Set to NONE since we don't build anything")
    hdr.PutLnIdn("project(MyInstallerProject NONE)")  

    hdr.PutLnIdn("# Set package properties\")")
    hdr.PutLnIdn("set(CPACK_PACKAGE_NAME \""+self["PACKAGE_NAME"]+"\")")
    hdr.PutLnIdn("set(CPACK_PACKAGE_VERSION \""+self["PACKAGE_VERSION"]+"\")")
    hdr.PutLnIdn("set(CPACK_PACKAGE_VENDOR \""+self["PACKAGE_VENDOR"]+"\")")
    hdr.PutLnIdn("set(CPACK_PACKAGE_DESCRIPTION \""+self["PACKAGE_DESCRIPTION"]+"\")")

    resources_dir = self["RESOURCES_DIR"]
    if resources_dir != None:
      hdr.PutLnIdn("set(CPACK_PRODUCTBUILD_RESOURCES_DIR \"" + resources_dir + "\")")

    icon_file = self["PACKAGE_ICON"]
    if icon_file != None:
      hdr.PutLnIdn("set(CPACK_PACKAGE_ICON \""+icon_file+"\")")
      hdr.PutLnIdn("set(CPACK_RESOURCE_FILE_ICON \""+icon_file+"\")")
      hdr.PutLnIdn("set(CPACK_PRODUCTBUILD_BACKGROUND \""+icon_file+"\")")
      hdr.PutLnIdn("set(CPACK_PRODUCTBUILD_BACKGROUND_ALIGNMENT bottomleft)")
      hdr.PutLnIdn("set(CPACK_PRODUCTBUILD_BACKGROUND_SCALING none)")

    readme_file = self["PACKAGE_README"]
    if readme_file != None:
      hdr.PutLnIdn("set(CPACK_RESOURCE_FILE_README \""+readme_file+"\")")
      
    license_file = self["PACKAGE_LICENSE"]
    if license_file != None:
      hdr.PutLnIdn("set(CPACK_PACKAGE_LICENSES \""+license_file+"\")")
      hdr.PutLnIdn("set(CPACK_PACKAGE_LICENSE_FILE \""+license_file+"\")")
      hdr.PutLnIdn("set(CPACK_RESOURCE_FILE_LICENSE \""+license_file+"\")")
      

    hdr.PutLnIdn("# Specify output file and packaging formats")
    hdr.PutLnIdn("if(APPLE)")
    if True:
      hdr.Indent()
      hdr.PutLnIdn("# Configure macOS package")
      hdr.PutLnIdn("set(CPACK_GENERATOR \"DragNDrop;productbuild\")")
      hdr.PutLnIdn("set(CPACK_DMG_VOLUME_NAME \"${CPACK_PACKAGE_NAME} ${CPACK_PACKAGE_VERSION}\")")
      hdr.PutLnIdn("set(CPACK_PRODUCTBUILD_IDENTIFIER \""+self["PACKAGE_BUNDLE_ID"]+"\")")
    
      first_comp = self.PutComponents(hdr)
      self.PutPreScript(hdr,first_comp);

      #hdr.PutLnIdn("set(CPACK_COMPONENT_ASSETS_REQUIRED TRUE)")

      hdr.PutLnIdn("set(CPACK_PACKAGING_INSTALL_PREFIX \"/\")")
      hdr.PutLnIdn("set(CPACK_COMPONENT_UNSPECIFIED_REQUIRED \"TRUE\")")

      #hdr.PutLnIdn("install(DIRECTORY " + dirs + " DESTINATION " + dest + " EXCLUDE_FROM_ALL)")
      #hdr.PutLnIdn("install(DIRECTORY Media/ DESTINATION Applications/MyApp/Media)")
      #hdr.PutLnIdn("install(DIRECTORY Assets/ DESTINATION Applications/MyApp/Assets)")

      #hdr.PutLnIdn("# For notarization")
      #hdr.PutLnIdn("set(CPACK_NOTARIZE_ON_UPLOAD TRUE)")
      #hdr.PutLnIdn("set(CPACK_NOTARIZE_USERNAME \"your_apple_id@example.com\")   # Change to your Apple ID")
      #hdr.PutLnIdn("set(CPACK_NOTARIZE_PASSWORD \"your_app_specific_password\")  # Change to your app-specific password")
      hdr.Dedent()

    hdr.PutLnIdn("elseif(WIN32)")
    if True:
      hdr.Indent()
      hdr.PutLnIdn("# Configure Windows package")
      hdr.PutLnIdn("set(CPACK_GENERATOR \"NSIS;ZIP\")")
    
      hdr.PutLnIdn("# Specify installation locations")
      first_comp = self.PutComponents(hdr)
      self.PutPreScript(hdr,first_comp);

      #hdr.PutLnIdn("install(DIRECTORY bundles/ DESTINATION \"C:/Program Files/MyApp\")")
      #hdr.PutLnIdn("install(DIRECTORY Media/ DESTINATION \"C:/Program Files/MyApp/Media\")")
      #hdr.PutLnIdn("install(DIRECTORY Assets/ DESTINATION \"C:/Program Files/MyApp/Assets\")")
      hdr.Dedent()
    hdr.PutLnIdn("endif()")

    hdr.PutLnIdn("include(CPack)")
    hdr.CloseFile()

    fn = self.build_and_package(working_dir,ctx["OUTPUT_DIR"])
    return fn


  def build_and_package(self,project_dir, output_dir):
    """
    Builds the CMake project at 'project_dir' and packages it using CPack.
    
    Args:
    - project_dir (str): The path to the project directory containing CMakeLists.txt.
    - output_dir (str): The directory where the .pkg file should be copied after packaging.
    """
    # Change to the specified directory
    os.chdir(project_dir)

    # Create the build directory with CMake
    subprocess.run(["cmake", "--trace", "-B", "build"], check=True)
    
    # Change to the build directory
    os.chdir("build")
    
    # Run CPack to create a .pkg file
    if sys.platform == "darwin": g = "productbuild"
    else: g = "NSIS"

    subprocess.run(["cpack", "--verbose", "-G", g], check=True)
    
    # Find the .pkg file generated by CPack
    # Assumes only one .pkg file is generated; adjust if necessary
    if sys.platform == "darwin":
      pkg_files = [f for f in os.listdir() if f.endswith('.pkg')]
      if not pkg_files:
          print("Error: No .pkg file was generated.")
          return
    else:  
      pkg_files = [f for f in os.listdir() if f.endswith('.exe')]
      if not pkg_files:
          print("Error: No .exe file was generated.")
          return
    result = ""
    # Copy the .pkg file to the specified output directory
    for pkg_file in pkg_files:
        src_path = os.path.join(os.getcwd(), pkg_file)  # Full source path of the .pkg file
        dest_path = os.path.join(output_dir, pkg_file)  # Combine output directory with the .pkg file name
        
        shutil.copy(src_path, dest_path)
        result = dest_path
        print(f"Copied {pkg_file} to {output_dir}")
    return result

class Context(InstallarNode):
  def __init__(self):
    super(Context,self).__init__()
  
  def sign_pkg(self, pkg_path, signed_pkg_path = "", xid = ""):
    if not os.path.exists(pkg_path):
        print(f"Error: The specified .pkg file does not exist: {pkg_path}")
        return ""
    if sys.platform != "darwin":
      # For windows this is a no-op
      return pkg_path

    if signed_pkg_path == "":    
      base, ext = os.path.splitext(pkg_path)
      base += "_signed"
      signed_pkg_path = base + ext

    print("Signing package " + pkg_path)    
    command = [
        "productsign", 
        "--sign", xid,  # Replace with your bundle ID
        pkg_path,
        signed_pkg_path
    ]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to sign package: {e}")
        return ""

    print("Package signed successfully to " + signed_pkg_path)    
    print("Verifying signed package " + signed_pkg_path)    
    command = [
        "pkgutil", "--check-signature", signed_pkg_path
    ]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to verify signature: {e}")
        return ""
    print("Package signature is verified.")    
    return signed_pkg_path    

  def notarize_pkg(self,pkg_path,keychain_profile_id):
    """
    Notarize a .pkg file using Apple's notarization service.
    
    Args:
        pkg_path (str): The file path of the .pkg file.
        apple_id (str): The Apple ID to use for notarization.
        app_specific_password (str): The app-specific password for notarization.
    """
    if not os.path.exists(pkg_path):
        print(f"Error: The specified .pkg file does not exist: {pkg_path}")
        return

    print("Submitting package for notarization...")
    # Submit the .pkg file for notarization
    command = ["xcrun", "notarytool", "submit", pkg_path,
                   "--keychain-profile", keychain_profile_id,
                   "--wait" ]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to submit for notarization: {e}")
        return False


    command = ["xcrun", "stapler", "staple", pkg_path]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to staple for notarization: {e}")
        return False
    print("Notarization request submitted. Checking status...")


  def make_dmg(self,pkg_file,dmg_file,vol_name):
      print("Removing old DMG (if exists)...")
      command = [
        "rm", "-f", dmg_file
      ]
      try:
        subprocess.run(command, check=True)
      except subprocess.CalledProcessError as e:
        print(f"Failed to remove old dmg: {e}")
        return False

      print("Creating disk image $DMG_FILE...")
      command = [
        "hdiutil", "create", "-fs", "HFS+", "-srcfolder", pkg_file, "-volname", vol_name, dmg_file
      ]
      try:
        subprocess.run(command, check=True)
      except subprocess.CalledProcessError as e:
        print(f"Failed to create dmg: {e}")
        return False
      return True  
