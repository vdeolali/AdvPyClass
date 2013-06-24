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

class Cls(dict):
    
    def __init__(cls,name, bases, body):
        cls['__name__'] = name
        cls['__bases__'] = bases
        exec dedent(body) in globals(), cls

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
    

############## CLIENT CODE ##########################
'going back in time before Python became OO'


Animal = Cls('Animal', (), '''
    'Demonstration of a simple Animal class'
    
    def __init__(inst,name):
       inst['name'] = name

    def walk(inst):
       print '{0} is walking'.format(inst['name'])
''')



Dog =  Cls('Dog', (Animal,), '''
'Specialization of Animal'

def bark(inst):
    print 'Woof'
''')

if __name__ == '__main__':
    d = Dog('Fido)
    d = make_inst(Dog, 'Fido')      #d = Dog('Fido')
    print inst_lookup(d, 'name')
    inst_lookup(d,'bark')()   #d.bark()
    inst_lookup(d,'walk')()   #d.walk()

    print d['__class__']['__bases__'][0]['__name__']  # print d.__
    
