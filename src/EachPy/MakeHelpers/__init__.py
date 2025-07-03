__revision__ = "1"
__version__ = "1.0.0"


def CheckSourceKind(x,kind):
        if (x == ".cpp") or (x == ".c") or (x == ".swift") or (x == ".pas"):
          kind = "src"
        elif (x == ".cxx") or (x == ".m") or (x == ".mm"):
          kind = "src"
        elif (x == ".py") or (x == ".js"):
          kind = "src"
        elif (x == ".h") or (x == ".hpp") or (x == ".hxx") or (x == ".inc"): kind = "hdr"
        elif (x == ".aif") or (x == ".aiff") or (x == ".wav") or (x == ".mp3"): kind = "res"
        elif x == ".png" or x == ".gif" or x == ".mp4": kind = "res"
        elif x == ".bmp": kind = "res"
        elif x == ".xcassets" or x == ".xcasset": kind = "res"
        elif x == ".xcprivacy": kind = "res"
        elif x == ".storyboard": kind = "res"
        #elif x == ".entitlements": kind = "res"
        elif x == ".framework": kind = "lib"
        elif x == ".tbd": kind = "lib"
        elif x == ".rc": kind = "res_src"
        elif x == ".md": kind = "ref"
        elif x == ".gog": kind = "res"
        elif x == ".morph": kind = "res"
        else: kind = "ref"  
        return kind


