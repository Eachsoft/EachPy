from . TextWriter import TextWriter

class FileWriter(TextWriter):
  def __init__(self, fn=""):
    super(FileWriter,self).__init__()
    self.fHandle = None
    if fn != "":
      import codecs
      self.fHandle = codecs.open(fn,"w","utf-8")

  def OpenFile(self, fn):
    import codecs
    self.fHandle = codecs.open(fn, "w", "utf-8")

  def Reset(self):
    self.CloseFile()
    self.IndentSize = 0

  def CloseFile(self):
    self.fHandle.close()

  def Put(self,s):
    self.fHandle.write(s)
    return self

  def PutLn(self,s):
    self.fHandle.write(s)
    self.fHandle.write("\n")
    return self
