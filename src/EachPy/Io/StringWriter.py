from . TextWriter import TextWriter
import io

class StringWriter(TextWriter):
  def __init__(self):
    super(StringWriter,self).__init__()
    self.fHandle = io.StringIO()

  def Reset(self):
    self.fHandle.close()
    self.fHandle = io.StringIO()
    self.fIndent = 0

  @property
  def Text(self):
    return self.fHandle.getvalue()

  def ToString(self): return self.fHandle.getvalue()

  def Put(self,s):
    #if type(s) is int: s = str(s)
    self.fHandle.write(s)
    return self

  def PutLn(self,s):
    h = self.fHandle
    h.write(s)
    h.write("\n")
    return self

  def CloseFile(self):
    self.fHandle.close()



