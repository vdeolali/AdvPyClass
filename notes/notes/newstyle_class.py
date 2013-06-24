class Cls(dict):

    def __init__(cls, name, bases, mapping):
        cls._name_ = name
        cls._bases_ = bases
        cls.update(mapping)

    def __getattr__(cls, attr):

        if attr in cls:
            return cls[attr]
        bases = cls._bases_
        # XXX Now does __mro__ search
        for base in bases:
            try:
                return getattr(base, attr)
            except AttributeError:
                pass
        raise AttributeError(attr)

    def __setattr__(cls, attr, value):
        cls[attr] = value

    def __delattr__(cls, attr, value):
        del cls[attr]

    def __call__(cls, *args):
        return Inst(cls, *args)

    def __repr__(cls):
        return '<Cls: %s>' % cls._name_

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
        if hasattr(result, '__get__'):
            return result.__get__(inst, cls)
        return result

    def __setattr__(inst, attr, value):
        inst[attr] = value

    def __delattr__(inst, attr, value):
        del inst[attr]

    def __repr__(inst):
        return '<Inst of %s>' % inst._class_._name_

class Object:
    __metaclass__ = Cls

############ CLIENT CODE #################################

class Animal(Object):

    'Demonstration of a simple Animal class'

    def _init_(inst, name):
        inst.name = name

    def walk(inst):
        print '{0} is walking'.format(inst.name)


class Dog(Animal):
    'Specialization of Animal'

    def bark(inst):
        print 'Woof!'

if __name__ == '__main__':

    d = Dog('Fido')                                  # d = Dog('Fido')
    print d.name                                     # print d.name
    d.bark()                                         # d.bark()   
    d.walk()                                         # d.walk()
    print d._class_._bases_[0]._name_                # print d._class_._bases_[0]._name_








    
