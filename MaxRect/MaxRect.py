# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_MaxRect')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_MaxRect')
    _MaxRect = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_MaxRect', [dirname(__file__)])
        except ImportError:
            import _MaxRect
            return _MaxRect
        try:
            _mod = imp.load_module('_MaxRect', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _MaxRect = swig_import_helper()
    del swig_import_helper
else:
    import _MaxRect
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _MaxRect.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _MaxRect.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _MaxRect.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _MaxRect.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _MaxRect.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _MaxRect.SwigPyIterator_equal(self, x)

    def copy(self):
        return _MaxRect.SwigPyIterator_copy(self)

    def next(self):
        return _MaxRect.SwigPyIterator_next(self)

    def __next__(self):
        return _MaxRect.SwigPyIterator___next__(self)

    def previous(self):
        return _MaxRect.SwigPyIterator_previous(self)

    def advance(self, n):
        return _MaxRect.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _MaxRect.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _MaxRect.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _MaxRect.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _MaxRect.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _MaxRect.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _MaxRect.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _MaxRect.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class VecDouble(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VecDouble, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VecDouble, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _MaxRect.VecDouble_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _MaxRect.VecDouble___nonzero__(self)

    def __bool__(self):
        return _MaxRect.VecDouble___bool__(self)

    def __len__(self):
        return _MaxRect.VecDouble___len__(self)

    def __getslice__(self, i, j):
        return _MaxRect.VecDouble___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _MaxRect.VecDouble___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _MaxRect.VecDouble___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _MaxRect.VecDouble___delitem__(self, *args)

    def __getitem__(self, *args):
        return _MaxRect.VecDouble___getitem__(self, *args)

    def __setitem__(self, *args):
        return _MaxRect.VecDouble___setitem__(self, *args)

    def pop(self):
        return _MaxRect.VecDouble_pop(self)

    def append(self, x):
        return _MaxRect.VecDouble_append(self, x)

    def empty(self):
        return _MaxRect.VecDouble_empty(self)

    def size(self):
        return _MaxRect.VecDouble_size(self)

    def swap(self, v):
        return _MaxRect.VecDouble_swap(self, v)

    def begin(self):
        return _MaxRect.VecDouble_begin(self)

    def end(self):
        return _MaxRect.VecDouble_end(self)

    def rbegin(self):
        return _MaxRect.VecDouble_rbegin(self)

    def rend(self):
        return _MaxRect.VecDouble_rend(self)

    def clear(self):
        return _MaxRect.VecDouble_clear(self)

    def get_allocator(self):
        return _MaxRect.VecDouble_get_allocator(self)

    def pop_back(self):
        return _MaxRect.VecDouble_pop_back(self)

    def erase(self, *args):
        return _MaxRect.VecDouble_erase(self, *args)

    def __init__(self, *args):
        this = _MaxRect.new_VecDouble(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _MaxRect.VecDouble_push_back(self, x)

    def front(self):
        return _MaxRect.VecDouble_front(self)

    def back(self):
        return _MaxRect.VecDouble_back(self)

    def assign(self, n, x):
        return _MaxRect.VecDouble_assign(self, n, x)

    def resize(self, *args):
        return _MaxRect.VecDouble_resize(self, *args)

    def insert(self, *args):
        return _MaxRect.VecDouble_insert(self, *args)

    def reserve(self, n):
        return _MaxRect.VecDouble_reserve(self, n)

    def capacity(self):
        return _MaxRect.VecDouble_capacity(self)
    __swig_destroy__ = _MaxRect.delete_VecDouble
    __del__ = lambda self: None
VecDouble_swigregister = _MaxRect.VecDouble_swigregister
VecDouble_swigregister(VecDouble)

class VecVecdouble(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VecVecdouble, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VecVecdouble, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _MaxRect.VecVecdouble_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _MaxRect.VecVecdouble___nonzero__(self)

    def __bool__(self):
        return _MaxRect.VecVecdouble___bool__(self)

    def __len__(self):
        return _MaxRect.VecVecdouble___len__(self)

    def __getslice__(self, i, j):
        return _MaxRect.VecVecdouble___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _MaxRect.VecVecdouble___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _MaxRect.VecVecdouble___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _MaxRect.VecVecdouble___delitem__(self, *args)

    def __getitem__(self, *args):
        return _MaxRect.VecVecdouble___getitem__(self, *args)

    def __setitem__(self, *args):
        return _MaxRect.VecVecdouble___setitem__(self, *args)

    def pop(self):
        return _MaxRect.VecVecdouble_pop(self)

    def append(self, x):
        return _MaxRect.VecVecdouble_append(self, x)

    def empty(self):
        return _MaxRect.VecVecdouble_empty(self)

    def size(self):
        return _MaxRect.VecVecdouble_size(self)

    def swap(self, v):
        return _MaxRect.VecVecdouble_swap(self, v)

    def begin(self):
        return _MaxRect.VecVecdouble_begin(self)

    def end(self):
        return _MaxRect.VecVecdouble_end(self)

    def rbegin(self):
        return _MaxRect.VecVecdouble_rbegin(self)

    def rend(self):
        return _MaxRect.VecVecdouble_rend(self)

    def clear(self):
        return _MaxRect.VecVecdouble_clear(self)

    def get_allocator(self):
        return _MaxRect.VecVecdouble_get_allocator(self)

    def pop_back(self):
        return _MaxRect.VecVecdouble_pop_back(self)

    def erase(self, *args):
        return _MaxRect.VecVecdouble_erase(self, *args)

    def __init__(self, *args):
        this = _MaxRect.new_VecVecdouble(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _MaxRect.VecVecdouble_push_back(self, x)

    def front(self):
        return _MaxRect.VecVecdouble_front(self)

    def back(self):
        return _MaxRect.VecVecdouble_back(self)

    def assign(self, n, x):
        return _MaxRect.VecVecdouble_assign(self, n, x)

    def resize(self, *args):
        return _MaxRect.VecVecdouble_resize(self, *args)

    def insert(self, *args):
        return _MaxRect.VecVecdouble_insert(self, *args)

    def reserve(self, n):
        return _MaxRect.VecVecdouble_reserve(self, n)

    def capacity(self):
        return _MaxRect.VecVecdouble_capacity(self)
    __swig_destroy__ = _MaxRect.delete_VecVecdouble
    __del__ = lambda self: None
VecVecdouble_swigregister = _MaxRect.VecVecdouble_swigregister
VecVecdouble_swigregister(VecVecdouble)

class PyLoc(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PyLoc, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PyLoc, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _MaxRect.new_PyLoc(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_setmethods__["first"] = _MaxRect.PyLoc_first_set
    __swig_getmethods__["first"] = _MaxRect.PyLoc_first_get
    if _newclass:
        first = _swig_property(_MaxRect.PyLoc_first_get, _MaxRect.PyLoc_first_set)
    __swig_setmethods__["second"] = _MaxRect.PyLoc_second_set
    __swig_getmethods__["second"] = _MaxRect.PyLoc_second_get
    if _newclass:
        second = _swig_property(_MaxRect.PyLoc_second_get, _MaxRect.PyLoc_second_set)
    def __len__(self):
        return 2
    def __repr__(self):
        return str((self.first, self.second))
    def __getitem__(self, index): 
        if not (index % 2):
            return self.first
        else:
            return self.second
    def __setitem__(self, index, val):
        if not (index % 2):
            self.first = val
        else:
            self.second = val
    __swig_destroy__ = _MaxRect.delete_PyLoc
    __del__ = lambda self: None
PyLoc_swigregister = _MaxRect.PyLoc_swigregister
PyLoc_swigregister(PyLoc)

class PyLocPair(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PyLocPair, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PyLocPair, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _MaxRect.new_PyLocPair(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_setmethods__["first"] = _MaxRect.PyLocPair_first_set
    __swig_getmethods__["first"] = _MaxRect.PyLocPair_first_get
    if _newclass:
        first = _swig_property(_MaxRect.PyLocPair_first_get, _MaxRect.PyLocPair_first_set)
    __swig_setmethods__["second"] = _MaxRect.PyLocPair_second_set
    __swig_getmethods__["second"] = _MaxRect.PyLocPair_second_get
    if _newclass:
        second = _swig_property(_MaxRect.PyLocPair_second_get, _MaxRect.PyLocPair_second_set)
    def __len__(self):
        return 2
    def __repr__(self):
        return str((self.first, self.second))
    def __getitem__(self, index): 
        if not (index % 2):
            return self.first
        else:
            return self.second
    def __setitem__(self, index, val):
        if not (index % 2):
            self.first = val
        else:
            self.second = val
    __swig_destroy__ = _MaxRect.delete_PyLocPair
    __del__ = lambda self: None
PyLocPair_swigregister = _MaxRect.PyLocPair_swigregister
PyLocPair_swigregister(PyLocPair)

class MaxRect(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MaxRect, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MaxRect, name)
    __repr__ = _swig_repr

    def __init__(self, arg2):
        this = _MaxRect.new_MaxRect(arg2)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _MaxRect.delete_MaxRect
    __del__ = lambda self: None

    def calMaxRect(self, arg2):
        return _MaxRect.MaxRect_calMaxRect(self, arg2)

    def getMaxRectLoc(self):
        return _MaxRect.MaxRect_getMaxRectLoc(self)

    def getMaxRectSize(self):
        return _MaxRect.MaxRect_getMaxRectSize(self)
MaxRect_swigregister = _MaxRect.MaxRect_swigregister
MaxRect_swigregister(MaxRect)

# This file is compatible with both classic and new-style classes.

