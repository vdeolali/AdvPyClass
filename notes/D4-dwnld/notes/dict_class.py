def __init__(inst, name):
    inst['name'] = name

def walk(inst):
    print '{0} is walking'.format(inst['name'])

Animal = {
    '__doc__': 'Demonstration of a simple Animal class',
    '__name__': 'Animal',
    '__bases__': (),
    '__init__': __init__,
    'walk': walk
}

def bark(inst):
    print 'Woof!'

Dog = {
    '__doc__': 'Specialization of Animal',
    '__name__': 'Dog',
    '__bases__': (Animal,),
    'bark': bark
}

if __name__ == '__main__':

    d = {'__class__': Dog,                           # d = Dog('Fido')
         'name': 'Fido'}

    print d['name']                                  # print d.name
    d['__class__']['bark'](d)                        # d.bark()
    d['__class__']['__bases__'][0]['walk'](d)        # d.walk()
    print d['__class__']['__bases__'][0]['__name__'] # print d.__class__.__bases__[0].__name__
    

