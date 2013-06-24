from functools import partial

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

'going back in time before Python became OO'

def __init__(inst,name):
    inst['name'] = name

def walk(inst):
    print '{0} is walking'.format(inst['name'])


Animal = {

    "__doc__": 'Demonstration of a simple animal',
    '__name__': 'Animal',
    '__bases__': (),
    '__init__': __init__,
    'walk': walk
    }

def bark(inst):
    print 'Woof'

Dog = {

    '__doc__': 'Specialization of Animal',
    '__name__': 'Dog',
    '__bases__': (Animal,),
    'bark': bark
    }


if __name__ == '__main__':
    d = make_inst(Dog, 'Fido')      #d = Dog('Fido')
    print inst_lookup(d, 'name')
    inst_lookup(d,'bark')()   #d.bark()
    inst_lookup(d,'walk')()   #d.walk()

    print d['__class__']['__bases__'][0]['__name__']  # print d.__
    
