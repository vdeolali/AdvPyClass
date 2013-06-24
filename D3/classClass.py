from functools import partial
from textwrap import dedent

def cls_lookup(cls,attr):
    try:
        return cls[attr]
    except KeyError:
        pass

    bases = cls['__bases__']
    for base in bases:
        try:
            return cls_lookup(base, attr)
        except AttributeError:
            pass
    raise AttributeError(attr)

class Inst(dict):

    def __init__(inst, cls, *args):
        inst._class_ = cls
        try:
            inst._init_(*args)
        except AttributeError:
            pass

    def __getattr__(inst, attr):
        if attr in inst:
            return inst[attr]
        cls = inst._class_
        result = getattr(cls, attr)
        if callable(result):
            return partial(result, inst)
        return result

    def __setattr__(inst, attr, value):
        inst[attr] = value

    def __repr__(inst):
        return '<Inst of %s>' % inst._class_._name_
        
def inst_lookup(inst, attr):
    try:
        return inst[attr]
    except KeyError:
        pass
    cls = inst['__class__']
    result = cls_lookup(cls,attr)
    if callable(result):
        return partial (result, inst)
    
    return result

def make_inst(cls, *args):
    inst = {}
    inst['__class__'] = cls
    try: 
        inst_lookup (inst, '__init__')(*args)
    except AttributeError:
        pass
    return inst

class Cls(dict):
    
    def __init__(cls,name, bases, mapping):
        cls['_name_'] = name
        cls['_bases_'] = bases
        cls.update(mapping)

    def __getattr__(cls,attr):
        try:
            return cls[attr]
        except KeyError:
            pass
        bases = cls['_bases_']

        for base in bases:
            try:
                return cls_lookup(base, attr)
            except AttributeError:
                pass
        raise AttributeError(attr)

    def __call__(cls,*args):
        return Inst(cls, *args)
    
    def __delattr__(cls, attr, value):
        del cla[attr]

    def __repr__(cls):
        return '<Cls:%s>' % cls._name_


class Object:
    __metaclass__ = Cls
    
############## CLIENT CODE ##########################


class Animal:
    __metaclass__ = Cls
    'Demonstration of a simple Animal class'
    def _init_(inst,name):
       inst['name'] = name
    def walk(inst):
       print '{0} is walking'.format(inst['name'])


class Dog (Animal):
    'Specialization of Animal'

    def bark(inst):
        print 'Woof'

if __name__ == '__main__':
    d = Dog('Fido')                                  # d = Dog('Fido')
    print d.name                                     # print d.name
    d.bark()                                         # d.bark()   
    d.walk()                                         # d.walk()
    print d._class_._bases_[0]._name_                # print d._class_._bases_[0]._name_

    
