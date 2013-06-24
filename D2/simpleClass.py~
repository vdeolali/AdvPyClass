class Animal:
    'Demonstration of a simple Animal class'

    def __init__(self, name):
        self.name = name

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


