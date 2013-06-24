'going back in time before Python became OO'

def __init__(self,name):
    inst['name'] = name

def walk(self):
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
    'bark':bark
    }


if __name__ == '__main__':
    d = {'__class__': Dog, 'name':'Fido'}

    print d['name']    #d.name
    print d['__class__']['bark'](d)   #d.bark()
    print d['__class__']['__bases__'][0]['__name__']  #d.walk()

    print d['__class__']['__bases__'][0]['__name__']  # print d.__
    
"""    
             

class Animal:
    'Demonstration of a simple Animal class'

    def __init__(self, name):
        print 'Start of Init:', vars(self)
        self.name = name
        print 'Start of Init:', vars(self)

    def walk(self):
        print '{0} is walking'.format(self.name)

class Dog(Animal):
    'Specialization of Animal'

    def bark(self):
        print 'Woof!'


if __name__ == '__main__':
    d = Dog('Fido')
    print d.name
    d.bark()
    d.walk()
    print d.__class__.__bases__[0].__name__
"""

