"""
Utlities to generate classes for Projucer.
"""
from collections import OrderedDict
import uuid
import string
import random
import os
import glob
import codecs
from filecmp import dircmp
import shutil
import html

import EachPy.Io
import EachPy.MakeHelpers as MakeHelpers


def escape_attr(s):
    s = html.escape(s)
    s = s.replace('\r', '&#13;')
    s = s.replace('\n', '&#10;')
    return s  


def JoinPathX(base,path):
  if path.find("$(") == 0: return path
  if path.find("/") == 0: return path
    #"/usr/include/freetype2",

  return os.path.join(base,path)
def RelPathX(path,base):
  if path.find("$(") == 0: return path
  return os.path.relpath(path,base)

def generate_juce_style_uuid():
    generated_uuid = uuid.uuid4()
    # Format the UUID with curly braces
    formatted_uuid = f"{{{str(generated_uuid).upper()}}}"    
    return formatted_uuid
    #return f'{{{uuid.uuid4().hex.upper()}}}'

def generate_node_id(length=6):
    characters = string.ascii_letters + string.digits  # Uppercase, lowercase, and digits
    return ''.join(random.choice(characters) for _ in range(length))

def get_attr_dict_str(dc):
    s = ""
    x = 0
    for k,v in dc.items():
      if x > 0: s += "\n"
      s += k
      if v != None: s += "=" + v
      x += 1
    return s

def get_attr_list_str(dc):
  return '\n'.join(dc)


def split_relative_path(relative_path):
    # Split the path into directory and filename
    directory, filename = os.path.split(relative_path)

    # If the directory is empty (no / characters), return just the filename
    if not directory:
        return [filename]

    # Split the directory into its components
    path_parts = directory.split(os.path.sep)  # Use the appropriate separator for the OS
    path_parts.append(filename)  # Add the filename to the end of the list
    return path_parts

def is_plain_relative_path(path):
    # Check if the path is empty
    if not path:
        return False
    
    # Check for absolute path conditions
    if path.startswith('/') or (len(path) >= 2 and path[1] == ':' and path[0].isalpha()):
        return False

    # Check if the path starts with one or more dot characters
    if path.startswith('.'):
        return False

    # Check if the path contains any forward or backslash characters
    if '/' in path or '\\' in path:
        return True

    return False

class XBaseNode:
  pass

class XAttrBaseNode:
  def __init__(self,ctx):
    self.Context = ctx
    self.DefsName = "defines"

  def add_path_attr(self,attr_name,path,base_path="",relative_to=""):
    # Compute relative path
    base_path = os.path.join(self.Context.SourceDir,base_path)
    path = JoinPathX(base_path,path)
    if relative_to != "":
      path = os.path.normpath(RelPathX(path,relative_to))

    # Add it
    self.add_attr_to_list(attr_name,path)

  def add_paths_attr(self,attr_name,paths,base_path="",relative_to=""):
    for path in paths:
      self.add_path_attr(attr_name,path,base_path,relative_to)

  def set_path_attr(self,attr_name,path,base_path="",relative_to=""):
    # Compute relative path
    base_path = os.path.join(self.Context.SourceDir,base_path)
    #base_path = self.Context.SourceDir)
    path = JoinPathX(base_path,path)
    if relative_to != "":
      path = os.path.normpath(RelPathX(path,relative_to))
    self.attrs[attr_name] = path


  #def AddIncPath(self,path,base_path=""): self.AddPathTo("headerPath",path,base_path)
  #def AddLibPath(self,path,base_path=""): self.AddPathTo("libraryPath",path,base_path)
  #def AddFrameworkSearchPath(self,path,base_path=""): self.AddPathTo("frameworkSearchPaths",path,base_path)
  #def AddIncPaths(self,paths,base_path=""):
  #  for path in paths:
  #    self.AddIncPath(path,base_path)
  #def AddLibPaths(self,paths,base_path=""):
  #  for path in paths:
  #    self.AddLibPath(path,base_path)
  #def AddFrameworkSearchPaths(self,paths,base_path=""):
  #  for path in paths:
  #    self.AddFrameworkSearchPath(path,base_path)

  #def set_path_attr(self,name,path,base_path=""):
  #  # Compute relative path
  #  base_path = os.path.join(self.Context.SourceDir,base_path)
  #  path = JoinPathX(base_path,path)
  #  path = os.path.normpath(RelPathX(path,self.Context.RelativeRootDir))
  #  self.attrs[name] = path

  def AddPathTo(self,name,path,base_path=""):
    # Compute relative path
    base_path = os.path.join(self.Context.SourceDir,base_path)
    path = JoinPathX(base_path,path)
    path = os.path.normpath(RelPathX(path,self.Context.RelativeRootDir))

    # Add it
    self.add_attr_to_list(name,path)

  def add_attr_to_list(self,attr_name,value):
    if not attr_name in self.attrs: self.attrs[attr_name] = []
    else:
      v = self.attrs[attr_name]
      if not (type(v) is list):
        self.attrs[attr_name] = []
    self.attrs[attr_name].append(value)

  def get_attr_as_dict(self,attr_name):
    if not attr_name in self.attrs: 
      self.attrs[attr_name] = OrderedDict()
    else:
      v = self.attrs[attr_name]
      if not (type(v) is OrderedDict):
        self.attrs[attr_name] = OrderedDict()
    return self.attrs[attr_name]

  def add_attr_to_dict(self,attr_name,name,value):
    self.get_attr_as_dict(attr_name)[name] = value
    #self.attrs[attr_name][name] = value

  def add_define(self,name,value=None):
    self.add_attr_to_dict("defines",name,value)

  @property
  def defs(self):
    return self.get_attr_as_dict(self.DefsName)

  def __getitem__(self, index):
        # Access the element at the given index in the _data list
        return self.attrs[index]

  def __setitem__(self, index, value):
        # Set the element at the given index in the _data list
        self.attrs[index] = value

  def __len__(self):
        # Return the length of the _data list
        return len(self.attrs)

  def trace_attrs(self,buf,attrs):
    x = 0
    put_line = False
    for k,v in attrs.items():
      if put_line:
        put_line = False
        buf.PutLn("")
        buf.PutIdn(' ' * 6)  

      #if k == "defines" or k == "headerPath" or k == "libraryPath" or k == "includes":
      #  self.LogError("Illegal attribute specified in attributes of " + type(self).__name__  + "(" + self.name + "). Attribute '" + k + "', value '" + v + "'") 
      s = v
      if type(v) is str: s = v
      elif type(v) is list:
        s = get_attr_list_str(v)
      elif type(v) is OrderedDict or type(v) is dict:
        s = get_attr_dict_str(v)
      else: 
        s = str(v)

      s = escape_attr(s)      
      need_line = len(s) > 20
      buf.Put(" "+k+"=\"" + str(s) + "\"")

      # ADd a line break if there are many on the line or if
      # it is defines or headerPath or something like that.
      if not need_line:
        x += 1
        if x > 2:
          need_line = True

      if need_line:
        x = 0
        put_line = True

class FileNode(XBaseNode):
  def __init__(self,path,rel_path,node_id,kind,ftype,_compile="0",resource="0"):
    super(FileNode,self).__init__()
    self.name    = os.path.basename(path)
    self.Path    = path
    # The path relative to the projucer project dir
    self.RelativePath    = rel_path
    self.NodeId  = node_id
    self.attrs   = OrderedDict()
    self.attrs["compile"] = _compile
    self.attrs["resource"] = resource

  def trace(self,buf):
    buf.Indent()
    buf.PutIdn("<FILE id=\"" + self.NodeId + "\" name=\""+self.name + "\"")
    for k,v in self.attrs.items():
      buf.Put(" "+k+"=\""+str(escape_attr(v))+"\"")
    buf.Put(" file=\""+escape_attr(self.RelativePath) + "\"")
    buf.PutLn(" />")
    buf.Dedent()

# Custom sort function: prioritize .h files over .cpp files
def custom_sort_key(obj):
    name = obj.name.lower()
    # Extension priority: .h files first, .cpp files second
    #return (ext_priority, name)  # Tuple: (priority, filename)
    base_name, ext = name.rsplit(".", 1)  # Split into base name and extension
    return (base_name,len(ext))

    #name = obj.name.lower()  # Make case insensitive
    #return name
    """
    ext_priority = 1 
    if ext == ".h": ext_priority = 0
    elif ext == ".hpp": ext_priority = 0
    elif ext == ".hxx": ext_priority = 0
    else: pass
    #ext_priority = 0 if extension == "h" else 1  # .h files get higher priority than .cpp
    return (base_name, ext_priority, ext)  # Sort by base name first, then prioritize by extension    
    """

class GroupNode(XBaseNode):
  def __init__(self,name,node_id,parent):
    super(GroupNode,self).__init__()
    self.name   = name
    self.NodeId = node_id
    self.Files  = []
    self.Groups = []
    self.attrs = OrderedDict()
    self.Parent = parent
    if parent != None:
      parent.Groups.append(self)


  def sort_all(self):
    sorted_files = sorted(self.Files, key=custom_sort_key)  # Case-insensitive sort
    self.Files = sorted_files
    sorted_groups = sorted(self.Groups, key=lambda obj: obj.name.lower())  # Case-insensitive sort
    self.Groups = sorted_groups
    for g in self.Groups:
      g.sort_all()

  def trace(self,buf):
    buf.Indent()
    if self.Parent != None: tag = "GROUP"
    else: tag = "MAINGROUP"
    buf.PutIdn("<"+tag+" id=\"" + self.NodeId + "\"")
    buf.Put(" name=\"" + self.name + "\"")
    buf.PutLn(" >")
    for item in self.Groups:
      item.trace(buf)
    for item in self.Files:
      item.trace(buf)
    buf.PutLnIdn("</"+tag+">")  
    buf.Dedent()

  def get_path(self):
    p = self.Parent
    if p != None:
      return p.get_path() + "/" + self.name
    else:
      return "/"   

  def get_path_with_sep(self):
    p = self.Parent
    if p != None:
      return p.get_path() + self.name + "/"
    else:
      return "/"   

class ConfigNode(XAttrBaseNode):
  def __init__(self,exporter,name,is_debug,targetName):
    super(ConfigNode,self).__init__(exporter.Context)
    self.name       = name
    self.Exporter   = exporter
    self.IsDebug    = is_debug
    self.attrs = OrderedDict()
    
    self.attrs["targetName"] = targetName
    if is_debug: v = 1
    else: v = 0
    self.attrs["isDebug"] = v
    self.attrs["name"] = name

    #self.attrs["binaryPath"] = ""
    #self.attrs["headerPath"] = []
    #self.attrs["libraryPath"] = []
    #self.attrs["defines"]                  = OrderedDict()
    #self.attrs["extraCompilerFlags"]       = []
    #self.attrs["extraLinkerFlags"]         = []
    #self.attrs["optimisation"]             = 0
    #self.attrs["linkTimeOptimisation"]     = 0
    #self.attrs["usePrecompiledHeaderFile"] = 0
    #self.attrs["precompiledHeaderFile"]    = str
    #self.attrs["enablePluginBinaryCopyStep"]    = 0
    #self.attrs["recommendedWarnings"] = 0 
    #self.attrs["iosBaseSDK"] = str
    #self.attrs["iosDeploymentTarget"] = "12.0"
    #self.attrs["iosCompatibility"] = str
    #self.attrs["customXcodeFlags"] = []
    #self.attrs["plistPreprocessorDefinitions"] = []
    #self.attrs["codeSigningIdentity"] = str
    #self.attrs["fastMath"] = 0
    #self.attrs["stripLocalSymbols"] = 0
    #self.attrs["userNotes"] = ""    

  def trace(self,buf):
    buf.Indent()
    buf.PutIdn("<CONFIGURATION")  
    self.trace_attrs(buf,self.attrs)
    buf.PutLn(" />")  
    buf.Dedent()


class JuceModule(XBaseNode):
  """
  Represents the MODULE entry for one of the Juce modules
  that will be included in the project.
  """

  def __init__(self,node_id,parent,
               relative_path,
               showAllCode="1",
               useLocalCopy="0",
               useGlobalPath="1"):
    super(JuceModule,self).__init__()
    self.NodeId = node_id
    self.attrs = OrderedDict()
    self.attrs["path"] = relative_path
    self.attrs["showAllCode"] = showAllCode
    self.attrs["useLocalCopy"] = useLocalCopy
    self.attrs["useGlobalPath"] = useGlobalPath

  def trace(self,buf):
    buf.Indent()
    buf.PutIdn("<MODULE id=\"" + self.NodeId + "\"")
    buf.Put(" showAllCode=\"" + self.attrs["showAllCode"] + "\"")
    buf.Put(" useLocalCopy=\"" + self.attrs["useLocalCopy"] + "\"")
    buf.Put(" useGlobalPath=\"" + self.attrs["useGlobalPath"] + "\"")
    buf.Put(" path=\"" + escape_attr(self.attrs["path"]) + "\"")
    buf.PutLn(" />")
    buf.Dedent()  

class ExporterNode(XAttrBaseNode):
  """
  Represents an exporter in the Projucer project, such as "Visual Studio 2022" or
  "XCode(iOS)" for example. Each exporter instance contains configurations for
  that target IDE or make system, such as Debug and Release.
  """
  def __init__(self,project,name):
    super(ExporterNode,self).__init__(project.Context)
    self.Project        = project
    self.name           = name
    self.Configs        = []
    self.attrs          = OrderedDict()
    self.DefsName       = "extraDefs"
    ctx = self.Context
    if name == "XCODE_MAC":
      s = ctx.BuildsDirName + "/MacOSX"
    elif name == "XCODE_IPHONE":
      s = ctx.BuildsDirName + "/iOS"
    elif name == "VS2022":
      s = ctx.BuildsDirNameWin + "/VisualStudio2022"
    elif name == "VS2019":
      s = ctx.BuildsDirNameWin+ "/VisualStudio2019"
    elif name == "LINUX_MAKE":
      s = ctx.BuildsDirNameLinux + "/LinuxMake"
    elif name == "ANDROIDSTUDIO":
      s = ctx.BuildsDirNameLinux + "/Android"
    else:
      sys.exit(1)  
    self.attrs["targetFolder"] = s

    for k,v in ctx.DefaultConfigs.items():
      config = ConfigNode(self,k,v["DEBUG"],self.Project.name)
      for kk,vv in v.items():
        if kk == "OPTIMIZE":
          config.attrs["optimisation"] = vv
      self.Configs.append(config)

  def add_custom_framework(self,framework):
    self.add_attr_to_list("extraCustomFrameworks",framework)
  def add_custom_frameworks(self,frameworks):
    for frame in frameworks:
      self.add_custom_framework(path,base_path)
  def add_lib(self,lib):
    self.add_attr_to_list("externalLibraries",lib)
  def add_libs(self,libs):
    for lib in libs:
      self.add_lib(lib)

  def add_define(self,name,value=None):
    self.add_attr_to_dict("extraDefs",name,value)

  def trace(self,project,buf):
    buf.Indent()
    buf.PutIdn("<" + self.name + "")
    self.trace_attrs(buf,self.attrs)
    buf.PutLn(" >")
    buf.Indent()
    buf.PutLnIdn("<CONFIGURATIONS>")
    for config in self.Configs:
      config.trace(buf)
    buf.PutLnIdn("</CONFIGURATIONS>")
    buf.PutLnIdn("<MODULEPATHS>")
    buf.Indent()
    for m in project.Modules:
      buf.PutIdn("<MODULEPATH id=\"" + m.NodeId + "\"")
      buf.Put(" path=\"" + m.attrs["path"] + "\"")
      buf.PutLn(" />")
    buf.Dedent()
      
    buf.PutLnIdn("</MODULEPATHS>")

    buf.Dedent()
    buf.PutLnIdn("</" + self.name + ">")
    buf.Dedent()

class JuceProject(XAttrBaseNode):
  """
  The JuceProject object represents a project that you can open and edit
  in the Projucer program. 
  """
  def __init__(self,ctx,name,projectType,exporters,projectName=None,pluginFormats=None,project_dir=None):
    """
    Parameters:
      ctx(Context): The JuceGen.Context object that will be the context for this project.
      name: The name of the project
    """
    super(JuceProject,self).__init__(ctx)
    # A list of all ids generated to make sure there are no duplicates
    self.AllIds = []
    self.NodeId = self.gen_node_id()
    self.name = name
    if projectName == None: 
      projectName = name
    self.ProjectName = projectName
    self.attrs = OrderedDict()
    self.juceoptions = OrderedDict()
    self.juceoptions["JUCE_STRICT_REFCOUNTEDPOINTER"] = "1"


    self.Modules = []
    self.Exporters = []

    # The node id for the main group is not a uuid
    self.MainGroup = GroupNode(name,self.gen_node_id(),None)
    self.CurrentGroup = self.MainGroup
    self.GroupStack = []

    if project_dir == None:
      if ctx.ProjectsInOwnDir:
        project_dir = os.path.join(ctx.WorkspaceDir,self.ProjectName)
      else:  
        project_dir = ctx.WorkspaceDir
    # Make sure the project dir exists
    os.makedirs(project_dir, exist_ok=True)
    # Make sure the project dir has a sub folder "JuceLibraryCode".
    juceLibraryCodeDirName = os.path.join(project_dir,ctx.JuceLibraryCodeDirName)
    os.makedirs(juceLibraryCodeDirName, exist_ok=True)

    self.JucerProjectDir = project_dir
    ctx.CurrentProjectDir = project_dir
    ctx.RelativeRootDir  = project_dir
    # Not really a dir, just a path that can be used to compute relative paths with.
    # This is needed for header and lib paths where projucer does not edit them.
    #ctx.BuildsOutputDir  = os.path.join(project_dir,"Source")
    ctx.BuildsOutputDir  = os.path.join(project_dir,ctx.BuildsDirName + "/AnyName")

    if projectType == None: 
      projectType = ctx.defs["projectType"]
    self.attrs["projectType"] = projectType

    self.attrs["pluginFormats"] = pluginFormats
    # Create the exporters
    if exporters  != None:
      for e in exporters:
        self.add_exporter(e)


  def set_default_attrs(self):
    self.attrs["addUsingNamespaceToJuceHeader"] = "0"
    self.attrs["useAppConfig"] = "0"
    self.attrs["jucerFormatVersion"] = "1"
    self.attrs["maxBinaryFileSize"] = 20971520

  

  def set_group(self, group):
    group = self.check_group_param(group)
    self.CurrentGroup = group
    return group

  def gen_xid(self):
    while True:
      s = generate_juce_style_uuid()
      if not s in self.AllIds:
        self.AllIds.append(s)
        return s
    return None    

  def gen_node_id(self):
    while True:
      s = generate_node_id()
      if not s in self.AllIds:
        self.AllIds.append(s)
        return s
    return None    

  def check_group_param(self,group):
    if group == None: 
      group = self.CurrentGroup
    elif type(group) is str: 
      return self.force_get_group(group)
    return group

  def sort_group(self,group):
    group = self.check_group_param(group)
    group.Sort()
    return group

  def sort_groups(self):
    g = self[ATT_GROUPS]
    g.sort(key=SortObjByNameFunc)

  def group_path(self):
     g = self.CurrentGroup  
     if g == None:
       return "/"
     return g.get_path_with_sep()


  def try_get_group(self,name,parent = None):
    slen = len(name)
    if slen > 1:
      if name[0] == "/":
        parent = self.MainGroup
    if parent == None: 
      parent = self.CurrentGroup  
    for item in parent.Groups:
      if item.name == name:
        return item
    return None    

  def force_get_group(self,name,parent = None):
    slen = len(name)
    if slen > 1:
      if name[0] == "/":
        parent = self.MainGroup

    if parent == None: 
      #parent = self.MainGroup  
      parent = self.CurrentGroup  

    return self.DoBuildGroupsFromPath(name,parent)

  def DoBuildGroupsFromPath(self,path,parent_group):
    sg = self.CurrentGroup
    items = path.split("/")
    ix = 0
    for item in items:
      if item != "/" and item != "":
        parent_group = self.add_group(item,parent_group)
    self.CurrentGroup = sg    
    return parent_group    

  def add_group(self,v,parent=None):
    if parent == None:
      parent = self.MainGroup
    elif type(parent) is str:
      parent = self.try_get_group(parent)
      if parent == None:
        sys.exit("Invalid group parent specified!")
    else:
      pass   

    if isinstance(v,GroupNode):
      #parent.Groups.append(v)
      self.CurrentGroup = v
      return v
    elif type(v) is list:
      vv = None
      for item in v:
        vv = self.add_group(item,parent)
      return vv
    elif type(v) is str:
      g = self.try_get_group(v,parent)
      if g != None:
        self.CurrentGroup = g
        return g
      gnode = GroupNode(v,self.gen_xid(),parent)  
      return self.add_group(gnode)
    else:
      assert False, "Unknown source group type supplied to add_group!"
      return None

  def add_file_ex(self,in_path,filter,group,kind,recurse):
    sg = self.CurrentGroup
    if '**' in filter:
      filter = filter.replace('**', '*')
      recurse = True
      sp = os.path.join(in_path, filter)
    sp = os.path.join(in_path, filter)
    files = glob.glob(sp)
    if True:
      for fn in files:
        if os.path.isfile(fn):
          self.add_file(fn,group,kind)
    else:
      sp = glob.glob(search_pattern)
      for file in os.listdir(in_path):
        if fnmatch.fnmatch(file,filter):
          fn = os.path.join(in_path,file)
          if os.path.isfile(fn):
            self.add_file(fn,group,kind)
    if recurse:
      if False:
        entries = os.listdir(in_path)
        directories = [entry for entry in entries if os.path.isdir(os.path.join(in_path, entry))] 
        for d in directories:     
          g = self.force_get_group(name,group)
          self.add_file_ex(path,filter,g,kind,True)
      else:
        for name in os.listdir(in_path):
          path = os.path.join(in_path, name)
          if os.path.isdir(path):
            g = self.force_get_group(name,group)
            self.add_file_ex(path,filter,g,kind,True)
    self.CurrentGroup = sg        


  def CheckPlainRelativePathToGroup(self,v,group):
    group = self.check_group_param(group)
    if type(v) is str:
      # Look for A/B/C/Filename.xyz so that A/B/C gets added to the group
      if is_plain_relative_path(v):
        parts = split_relative_path(v)
        xlen = len(parts)
        if xlen > 1:
          xlen -= 1
          x = 0
          while x < xlen:
            part = parts[x]
            if all(c.isalnum() or c == '_' for c in part):
              group = self.force_get_group(part,group)
            else: break
            x += 1
    return group        

  def add_file(self,v,group=None,kind="",ftype=""):
    group = self.CheckPlainRelativePathToGroup(v,group)
    if isinstance(v,FileNode):
      group.Files.append(v)
      return v
    if type(v) is list:
      vv = None
      for item in v:
        vv = self.add_file(item,group,flags)
      return vv
    elif type(v) is str:
      nm = os.path.basename(v)
      nmlen = len(nm)
      if nmlen == 0: return None
      if nm[0] == ".": return None
      ix = nm.find(";")
      is_filter = '|' in nm or '*' in nm
      if is_filter:
        dc = nm.split("|")
        is_recurse = False
        for d in dc:
          if d == "-R":
            is_recurse = True
        for d in dc:
          nm = os.path.dirname(v)
          self.add_file_ex(nm,d,group,kind,is_recurse)
        return None

      
      rel = RelPathX(v, self.JucerProjectDir)  
      _compile = "0"
      resource = "0"
      if kind == "src" or kind == "*" or kind == "" or kind == None:
        other_, extension = os.path.splitext(v)
        kind = MakeHelpers.CheckSourceKind(extension,v)

      if kind == "src": _compile = "1"
      elif kind == "res": resource = "1"

      fnode = FileNode(v,rel,self.gen_node_id(),kind,ftype,_compile,resource)
      return self.add_file(fnode,group)
    else:
      assert False, "Unknown source type supplied to add_file!"
      return None

  def add_folder(self,folder_name,filters,kind=""):
    if group == ".": group = self.group_path() + folder_name 
    self.add_files(folder_name + "/" + filters,path="",group=group,kind=kind)

  def add_resources(self,files,path="",group=None,ftype=""):
    self.add_files(files,path,group,"res",ftype)

  def add_file_refs(self,files,path="",group=None,ftype=""):
    self.add_files(files,path,group,"ref",ftype)

  def add_files(self,files,path="",group=None,kind="",ftype=""):
    sg = self.CurrentGroup
    if group == None:
      group = self.CurrentGroup
    else: group = self.check_group_param(group)  

    path=os.path.join(self.Context.SourceDir,path)
    if files != None:
      if type(files) is str:
        group = self.CheckPlainRelativePathToGroup(files,group)
        self.add_file(JoinPathX(path,files),group,kind,ftype)
      else:  
        for item in files:
          new_group = self.CheckPlainRelativePathToGroup(item,group)
          self.add_file(JoinPathX(path,item),new_group,kind,ftype)
    self.CurrentGroup = sg      

  def require_juce_module(self,module_name,showAllCode="1",useLocalCopy="0",useGlobalPath="1"):
    relPath = RelPathX(self.Context.JuceModulesDir,self.JucerProjectDir)
    module = JuceModule(module_name,self,relPath,showAllCode,useLocalCopy,useGlobalPath)  
    self.Modules.append(module)
    return module

  def add_default_juce_modules(self):
    project_type = self.attrs["projectType"]
    if project_type == "audioplug":
      self.require_juce_module("juce_audio_basics")
      self.require_juce_module("juce_audio_devices")
      self.require_juce_module("juce_audio_formats")
      self.require_juce_module("juce_audio_plugin_client")
      self.require_juce_module("juce_audio_processors")
      self.require_juce_module("juce_audio_utils")
      self.require_juce_module("juce_core")
      self.require_juce_module("juce_data_structures")
      self.require_juce_module("juce_events")
      self.require_juce_module("juce_graphics")
      self.require_juce_module("juce_gui_basics")
      self.require_juce_module("juce_gui_extra")
    elif project_type == "guiapp":
      self.require_juce_module("juce_core")
      self.require_juce_module("juce_data_structures")
      self.require_juce_module("juce_events")
      self.require_juce_module("juce_graphics")
      self.require_juce_module("juce_gui_basics")
      self.require_juce_module("juce_gui_extra")
    elif project_type == "consoleapp":
      self.require_juce_module("juce_core")
      self.require_juce_module("juce_data_structures")
      self.require_juce_module("juce_events")
    else:
      self.require_juce_module("juce_core")
      self.require_juce_module("juce_data_structures")
      self.require_juce_module("juce_events")
      self.require_juce_module("juce_graphics")
      self.require_juce_module("juce_gui_basics")
      self.require_juce_module("juce_gui_extra")



  def trace(self,buf):
    buf.PutLnIdn("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
    buf.PutIdn("<JUCERPROJECT id=\"" + self.NodeId + "\"")
    buf.Put(" name=\"" + self.name + "\"")
    #buf.Put(" projectType=\"" + self.ProjectType + "\"")
    self.trace_attrs(buf,self.attrs)
    buf.PutLn(" >")  
    buf.Indent()
    if True:
      self.MainGroup.sort_all()
      self.MainGroup.trace(buf)

      buf.PutLnIdn("<MODULES>")
      buf.Indent()
      for m in self.Modules:
        m.trace(buf)
      buf.Dedent()
      buf.PutLnIdn("</MODULES>")
    
      buf.PutIdn("<JUCEOPTIONS ")
      self.trace_attrs(buf,self.juceoptions)
      buf.PutLnIdn(" />")
      
      buf.PutLnIdn("<EXPORTFORMATS>")
      buf.Indent()
      for item in self.Exporters:
        item.trace(self,buf)

      buf.Dedent()
      buf.PutLnIdn("</EXPORTFORMATS>")

    buf.Dedent()
    buf.PutLnIdn("</JUCERPROJECT>")
  
  def add_exporter(self,name):
    e = ExporterNode(self,name)
    self.Exporters.append(e)
    return e

  def has_exporter(self,name):  
    if not type(name) is list: name = [name]
    for n in name:
      for e in self.Exporters:
        if e.name == n:
          return True
    return False

  def save(self):
    fn = os.path.join(self.JucerProjectDir, self.ProjectName + ".jucer")
    buf = EachPy.Io.FileWriter(fn)
    self.trace(buf)

  ##def RelPath(self,path):
  #  return os.path.relpath(path,self.ProjectDir)  


class Context:
  """
  The context object stores some state variables that are used during the creation
  of the juce projects and the objects inside them, such as files and configurations.
  It is the first object that is created and then passed to the constructor of each
  project that you create so that the project knows basically how to compute
  relative file paths and where everything is in the system. 
  """
  def __init__(self,source_dir,juce_dir,workspace_dir=None):
    if workspace_dir == None:
      workspace_dir = os.path.normpath(os.path.join(os.getcwd(),"JucerWorkspace"))
    self.attrs = OrderedDict()  
    self.WorkspaceDir   = workspace_dir
    self.SourceDir      = source_dir
    self.JuceDir        = juce_dir
    self.attrs["SourceDir"] = source_dir
    self.attrs["JuceDir"] = juce_dir
    self.JuceModulesDir = os.path.join(self.JuceDir,"modules")
    self.BuildsDirName  = "Builds"
    self.BuildsDirNameWin  = "BuildsWin"
    self.BuildsDirNameLinux  = "BuildsLinux"
    self.JuceLibraryCodeDirName  = "JuceLibraryCode"
    self.ProjectsInOwnDir = False
    self.CurrentJucerProjectDir = None
    self.RelativeRootDir = None
    self.DefaultConfigs   = {"Debug": {"DEBUG": True, "OPTIMIZE": "1"},
                             "Release": {"DEBUG": False, "OPTIMIZE": "6"}}
    self.SourceDirStack = []
    self.RelativeRootStack = []

  def join_source_dir(self,path):
    return os.path.join(self.SourceDir,path)
    #return os.path.relpath(path,self.SourceDir)

  def set_source_dir(self,path):
    #s = os.path.join(self.SourceDir,path)
    self.SourceDir = self.join_source_dir(path)
    return self.SourceDir


  def __getitem__(self, index):
        # Access the element at the given index in the _data list
        return self.attrs[index]

  def __setitem__(self, index, value):
        # Set the element at the given index in the _data list
        self.attrs[index] = value

  def __len__(self):
        # Return the length of the _data list
        return len(self.attrs)
