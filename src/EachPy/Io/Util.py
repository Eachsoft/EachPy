import sys
import Cx.PyVer as PyVer

def InputQuery(s):
  if PyVer.Has_input_function:
    return input(s)
  else:
    return raw_input(s)

def FileToString(fn):
  import codecs
  s = ""
  with codecs.open (fn, "r", "utf-8") as myfile:
    s=myfile.read()
    myfile.close()
  return s+""

def StringToFile(s,fn):
  import codecs
  with codecs.open (fn, "w", "utf-8") as myfile:
    myfile.write(s)
    myfile.flush()
    myfile.close()


