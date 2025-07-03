__version__ = '1.0'

import sys
import io
import os
import imp
import fnmatch

def SubDirForFn(fn,subdir):
  return ExtractFilePath(fn) + "/" + subdir

def IsPathStr(s):
  xlen = len(s)
  if xlen > 0:
    if s[0] == "/":
      if os.name == "nt":
        return False
      return True
    elif s[0].isalpha():
      if xlen == 2:
        # drive letter and colon only
        if s[1] == ":":
          return True
      elif xlen > 2:
        if s[1] == ":":
          # test for c:\
          if xlen > 3:
            c = s[2]
            if c == "/" or c == "\\":
              return True
        elif s[1].isalpha():
          # look for http://
          x = 1
          while (x < xlen) and s[x].isalpha():
            x+=1
          if (x < xlen):
            if s[x] == ":":
              x += 1
              if x < xlen:
                if c == "/" or c == "\\":
                  return True
    else:
      return False  
  return False

def CheckPathX(fn,base):
  if IsPathStr(fn): return fn
  #print(fn)
  #print(base)
  if base == "": base = str(os.getcwd()) + "/"
  s = os.path.join(base, fn)
  #print(s)
  return s

def CheckPath(fn):
  if IsPathStr(fn): return fn
  base = str(os.getcwd()) + "/"
  #print(base)
  s = os.path.join(base, fn)
  #print(s)
  return s
  
def ExtractFilePath(fn):
  return os.path.dirname(fn)

def ExtractPath(fn):
  return os.path.dirname(fn)

def ExtractFileName(fn):
  return os.path.basename(fn)
  # Was this? Is pY2? return os.path.filename(fn)

def ExtractFileExt(fn):
  path,ext = os.path.splitext(fn)
  return ext

def ChangeFileExt(fn,new_ext):
  path,ext = os.path.splitext(fn)
  return path + new_ext

def ExtractFileExtPlain(fn):
  path,ext = os.path.splitext(fn)
  if len(ext) > 0:
    if ext[0] == ".":
      ext = ext[1:]
  return ext

def MakeAbsPath(fn,path):
  return os.path.abspath(os.path.join(fn, path))

def MakeRelPathToFn(fn,rel_path):
  return MakeAbsPath(ExtractFilePath(fn), rel_path)

def JoinPath(a,b):
  return os.path.abspath(os.path.join(ExtractFilePath(a), b))

def ForcePath(path):
  return os.makedirs(path,exist_ok=True)

def IsDir(fn):
  return os.path.isdir(fn)

def IsFile(fn):
  return os.path.isfile(fn)

def GetFilesInDir(in_path, filter):
  result = []
  for file in os.listdir(in_path):
    if fnmatch.fnmatch(file,filter):
      result.append(file)
  return result

def GetFilesInDirEx(in_path, filter, recurse = True, sorted = False):
  result = []
  for file in os.listdir(in_path):
    if fnmatch.fnmatch(file,filter):
      fn = os.path.join(in_path,file)
      if os.path.isfile(fn):
        result.append(fn)
  if recurse:
    for name in os.listdir(in_path):
      path = os.path.join(in_path, name)
      if os.path.isdir(path):
        items = GetFilesInDirEx(path,filter,True)
        for item in items:
          result.append(item)
  if sorted: 
    result.sort()        
  return result

def FixPath(s):
  x = len(s)
  if x > 0:
    c = s[x-1]
    if c != "/" and c != "\\":
      return s + "/"
  return s  

def GetFilesInDirWithPath(in_path, filter):
  result = []
  for file in os.listdir(in_path):
    if	 fnmatch.fnmatch(file,filter):
      fn = in_path + "/" + file
      result.append(fn)
  return result

def GetDirsInDir(dir):
  result = []
  for name in os.listdir(dir):
    path = os.path.join(dir, name)
    if os.path.isdir(path):
      result.append(name)
  return result

def GetDirsInDirWithPath(dir):
  result = []
  for name in os.listdir(dir):
    path = os.path.join(dir, name)
    if os.path.isdir(path):
      result.append(path)
  return result



