import sys
import types

enable_gui = True
Tkinter = None
try:
    import Tkinter
except ImportError:
    try:
        import tkinter as Tkinter
    except:
        enable_gui = False

PY3 = sys.version_info[0] == 3

if PY3: # pragma: no cover
    string_types = str,
    integer_types = int,
    class_types = type,
    text_type = str
    binary_type = bytes
    long = int
else:
    string_types = basestring,
    integer_types = (int, long)
    class_types = (type, types.ClassType)
    text_type = unicode
    binary_type = str
    long = long

def text_(s, encoding='latin-1', errors='strict'):
    """ If ``s`` is an instance of ``binary_type``, return
    ``s.decode(encoding, errors)``, otherwise return ``s``"""
    if isinstance(s, binary_type):
        return s.decode(encoding, errors)
    return s # pragma: no cover

def bytes_(s, encoding='latin-1', errors='strict'):
    """ If ``s`` is an instance of ``text_type``, return
    ``s.encode(encoding, errors)``, otherwise return ``s``"""
    if isinstance(s, text_type): # pragma: no cover
        return s.encode(encoding, errors)
    return s

def print_(*args):
    x = " ".join(args)
    if x:
        sys.stdout.write(x)
    sys.stdout.write("\n")

