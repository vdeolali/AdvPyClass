from functools import partial
from textwrap import dedent

class Inst(dict):

    def __init__(inst, cls, *args):
        inst._class_ = cls
        try:
            inst._init_(*args)
        except AttributeError:
            pass

    def __getattr__(inst, attr):
        try:
            return inst[attr]
        except KeyError:
            pass
        cls = inst._class_
        result = getattr(cls, attr)
        if callable(result):
            return partial(result, inst)
        return result

    def __setattr__(inst, attr, value):
        inst[attr] = value

class Cls(dict):

    def __init__(cls, name, bases, body):
        cls._name_ = name
        cls._bases_ = bases
        exec dedent(body) in globals(), cls

    def __getattr__(cls, attr):
        try:
            return cls[attr]
        except KeyError:
            pass
        bases = cls._bases_
        for base in bases:
            try:
                return getattr(base, attr)
            except AttributeError:
                pass
        raise AttributeError(attr)

    def __setattr__(cls, attr, value):
        cls[attr] = value

    def __call__(cls, *args):
        return Inst(cls, *args)

############ CLIENT CODE #################################

Animal = Cls('Animal', (), '''
    'Demonstration of a simple Animal class'

    def _init_(inst, name):
        inst.name = name

    def walk(inst):
        print '{0} is walking'.format(inst.name)
''')

Dog = Cls('Dog', (Animal,), '''
    'Specialization of Animal'

    def bark(inst):
        print 'Woof!'
''')

if __name__ == '__main__':

    d = Dog('Fido')                                  # d = Dog('Fido')
    print d.name                                     # print d.name
    d.bark()                                         # d.bark()   
    d.walk()                                         # d.walk()
    print d._class_._bases_[0]._name_                # print d._class_._bases_[0]._name_








    
