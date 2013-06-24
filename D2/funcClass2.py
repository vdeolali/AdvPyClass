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

def make_class(name, bases, body):
    cls = {}
    cls['__name__'] = name
    cls['__bases__'] = bases
    exec dedent(body) in globals(), cls
    return cls

'going back in time before Python became OO'


Animal = make_class('Animal', (), '''
    'Demonstration of a simple Animal class'
    
    def __init__(inst,name):
       inst['name'] = name

    def walk(inst):
       print '{0} is walking'.format(inst['name'])
''')



Dog =  make_class ('Dog', (Animal,), '''
'Specialization of Animal'

def bark(inst):
    print 'Woof'
''')

if __name__ == '__main__':
    d = make_inst(Dog, 'Fido')      #d = Dog('Fido')
    print inst_lookup(d, 'name')
    inst_lookup(d,'bark')()   #d.bark()
    inst_lookup(d,'walk')()   #d.walk()

    print d['__class__']['__bases__'][0]['__name__']  # print d.__
    
