

class TextWriter(object):
  def __init__(self):
    super(TextWriter,self).__init__()
    self.IndentSize = 0
    self.fHandle = None

  def Indent(self):
    self.IndentSize += 2
    return self
    
  def Dedent(self):
    self.IndentSize -= 2
    return self

  def PutIdn(self,s):
    self.Put(' ' * self.IndentSize)
    self.Put(s)
    return self

  def PutLnIdn(self,s):
    self.Put(' ' * self.IndentSize)
    self.PutLn(s)
    return self

  def PutLn(self,s):
    self.fHandle.write(s)
    self.fHandle.write("\n")
    return self



