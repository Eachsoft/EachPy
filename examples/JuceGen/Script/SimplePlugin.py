import os
import JuceGen
import ExamplesConfig

def generate_config(ctx,project,exporter,config,plugin_name):
  if config.IsDebug:
    config.defs["DEBUG"] = "1"  
    config.defs["_DEBUG"] = "1"  
  else:
    config.attrs["optimisation"] = "6"  

  en = exporter.Name
  binary_products_base = "../../../bin/"
  config.attrs["binaryPath"] = binary_products_base + "Examples/JuceGen/" + project.Name + "/" + en + "/" + config.Name 

def generate_exporter(ctx,project,exporter,plugin_name):
  """
  The exporter object is one of the exporters as it would be
  in Projucer, such as Visual Studio 2022, or Mac OSX.
  """
  en = exporter.Name
  # Attributes can be set per exporter type such as
  if en in ["XCODE_MAC","XCODE_IPHONE"]:
    pass
  else:
    # Need to set the aax sdk path. Is relative from the Juce path to 
    # the folder where the final generated ide project will be.
    exporter.set_path_attr("aaxFolder",
                       "modules/juce_audio_plugin_client/AAX/SDK",
                       ctx["JuceDir"],
                       relative_to=project.JucerProjectDir)


  if en in ["XCODE_MAC","XCODE_IPHONE"]:
    exporter.defs["PROJECT_VERSION"]="$(CURRENT_PROJECT_VERSION)"
    exporter.defs["MY_BUNDLE_IDENTIFIER"]="\"$(PRODUCT_BUNDLE_IDENTIFIER)\""

  if en in ["XCODE_IPHONE"]:
    s = "CODE_SIGN_IDENTITY=\"Apple Development\"\n"
    s += "CODE_SIGN_STYLE=Automatic\n"
    exporter.attrs["customXcodeFlags"] = s

    exporter["UISupportsDocumentBrowser"] = "1"
    exporter["UIFileSharingEnabled"] = "1"
    exporter["duplicateAppExResourcesFolder"] = "0"
    exporter["iosAppGroups"]="1" 

    # Here is how to put other resources inside the XCode bundle
    # without needing to use Juce binary data in cpp.
    exporter.set_path_attr("customXcodeResourceFolders",
                           "examples/JuceGen/SimplePlugin/Media",
                           ctx["SourceDir"],
                           relative_to=project.JucerProjectDir)


  elif en in ["ANDROIDSTUDIO"]:
    # Here is how to get a lot of files into the android 
    # project without using juce cpp binary resources.
    exporter.set_path_attr("androidExtraAssetsFolder",
                           "examples/JuceGen/SimplePlugin/Media",
                           ctx["SourceDir"],
                           relative_to=project.JucerProjectDir)
    exporter["microphonePermissionNeeded"]="1"
    exporter["androidScreenOrientation"]="landscape"


  # For each config in the exporter, pass it to the config handling function.
  # For example, Debug and Release.
  for config in exporter.Configs:
    generate_config(ctx,project,exporter,config,plugin_name)

  return

def generate_project(project):
  ctx = project.Context
  print("Making plugin " + project.name)
  plugin_name = ctx["PLUGIN_NAME"]

  # Options of the project are set with the juce_options dictionary
  # These correspond to the JUCEOPTIONS element of the projucer file
  project.juceoptions["JUCE_VST3_CAN_REPLACE_VST2"]="0" 
  project.juceoptions["JUCE_PLUGINHOST_VST"]="1" 
  project.juceoptions["JUCE_PLUGINHOST_VST3"]="1" 
  project.juceoptions["JUCE_PLUGINHOST_AU"]="1"

  # Set attributes of the project object. Attributes can be set
  # using the indexer syntax of the project object, or the attrs
  # property of the project object.
  project.set_default_attrs()
  # The attribute companyName could be written as...
  project["companyName"]        = "MyHandle"
  # or write it like so...
  project.attrs["companyName"]        = "MyHandle"

  project["companyWebsite"]     = "www.myhandle.com"
  project["pluginManufacturer"] = "MyHandle"
  project["pluginAUMainType"]   = "'aufx'"
  project["pluginAAXCategory"]  = 8192

  project["pluginName"] = plugin_name
  project["pluginManufacturerCode"] = "VST "
  project["pluginCode"] = "MYPL"

  project["aaxIdentifier"] = "com.myhandle.simpleplugin"
  project["version"] = "0.1.0" 
  project["bundleIdentifier"] = "com.myhandle.simpleplugin"
  project["pluginCharacteristicsValue"] = "pluginProducesMidiOut,pluginWantsMidiIn" 

  # Set macro preprocessor definitions here. This is done using the defs property of the project object.
  # In the generated file for the Ide these will be the preprocessor definitions that are
  # available in the source code.
  project.defs["PLUGIN_NAME"]            = plugin_name

  # Header file search paths
  paths = ["examples/JuceGen/SimplePlugin/Source",
           ExamplesConfig.VST3SDK_DIR]
  project.add_paths_attr("headerPath",paths,
                      base_path=ctx["SourceDir"],
                      relative_to=ctx.BuildsOutputDir)    


  cxx_filters_deep = "**.cpp|**.h|**.hpp|**.hxx|**.cxx|**.mm|**.c"
  # Add the source files
  files = ["examples/JuceGen/SimplePlugin/Source/" + cxx_filters_deep]
  project.add_files(files,group="/" + plugin_name + "/")

  # Add resource files if any
  ctx.set_source_dir(ctx["SourceDir"])
  project.add_resources("examples/JuceGen/Graphics/**.jpeg",group="/" + plugin_name + "/Graphics")

  # Add Juce modules
  project.add_default_juce_modules()

  for exporter in project.Exporters:
    generate_exporter(ctx,project,exporter,plugin_name)

  return project

def make_plugin(plugin_name):
  root_dir = os.path.normpath(os.path.join(os.path.dirname(__file__),"../../../"))

  # The path to the output folder where the .projucer files will go
  proj_root_dir = os.path.join(root_dir,"bld/JuceExamples/" + plugin_name)

  # Make a context so that variables can be passed around easily
  ctx = JuceGen.Context(root_dir,ExamplesConfig.JUCE_DIR,proj_root_dir)
  ctx["ProjSourceDir"] = proj_root_dir
  ctx["PLUGIN_NAME"]   = plugin_name

  # Generate the project
  generate_project(JuceGen.JuceProject(ctx,plugin_name,"audioplug",["XCODE_MAC","XCODE_IPHONE","VS2019","VS2022","LINUX_MAKE","ANDROIDSTUDIO"],
                                projectName=plugin_name,
                                pluginFormats="buildVST3,buildAU,buildAUv3,buildAAX,buildVST,buildStandalone")).save()

if __name__ == "__main__":
  make_plugin("SimplePlugin")


