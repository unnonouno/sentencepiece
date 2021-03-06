# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_sentencepiece', [dirname(__file__)])
        except ImportError:
            import _sentencepiece
            return _sentencepiece
        if fp is not None:
            try:
                _mod = imp.load_module('_sentencepiece', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _sentencepiece = swig_import_helper()
    del swig_import_helper
else:
    import _sentencepiece
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SentencePieceProcessor(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SentencePieceProcessor, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SentencePieceProcessor, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _sentencepiece.new_SentencePieceProcessor()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sentencepiece.delete_SentencePieceProcessor
    __del__ = lambda self : None;
    def Load(self, *args): return _sentencepiece.SentencePieceProcessor_Load(self, *args)
    def LoadOrDie(self, *args): return _sentencepiece.SentencePieceProcessor_LoadOrDie(self, *args)
    def SetEncodeExtraOptions(self, *args): return _sentencepiece.SentencePieceProcessor_SetEncodeExtraOptions(self, *args)
    def SetDecodeExtraOptions(self, *args): return _sentencepiece.SentencePieceProcessor_SetDecodeExtraOptions(self, *args)
    def GetPieceSize(self): return _sentencepiece.SentencePieceProcessor_GetPieceSize(self)
    def PieceToId(self, *args): return _sentencepiece.SentencePieceProcessor_PieceToId(self, *args)
    def IdToPiece(self, *args): return _sentencepiece.SentencePieceProcessor_IdToPiece(self, *args)
    def GetScore(self, *args): return _sentencepiece.SentencePieceProcessor_GetScore(self, *args)
    def IsUnknown(self, *args): return _sentencepiece.SentencePieceProcessor_IsUnknown(self, *args)
    def IsControl(self, *args): return _sentencepiece.SentencePieceProcessor_IsControl(self, *args)
    def Encode(self, *args): return _sentencepiece.SentencePieceProcessor_Encode(self, *args)
    def EncodeAsPieces(self, *args): return _sentencepiece.SentencePieceProcessor_EncodeAsPieces(self, *args)
    def EncodeAsIds(self, *args): return _sentencepiece.SentencePieceProcessor_EncodeAsIds(self, *args)
    def Decode(self, *args): return _sentencepiece.SentencePieceProcessor_Decode(self, *args)
    def DecodePieces(self, *args): return _sentencepiece.SentencePieceProcessor_DecodePieces(self, *args)
    def DecodeIds(self, *args): return _sentencepiece.SentencePieceProcessor_DecodeIds(self, *args)
    def __len__(self): return _sentencepiece.SentencePieceProcessor___len__(self)
    def __getitem__(self, *args): return _sentencepiece.SentencePieceProcessor___getitem__(self, *args)
SentencePieceProcessor_swigregister = _sentencepiece.SentencePieceProcessor_swigregister
SentencePieceProcessor_swigregister(SentencePieceProcessor)

# This file is compatible with both classic and new-style classes.


