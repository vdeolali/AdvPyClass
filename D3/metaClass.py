'''

* type. __new__ make the class
* type.__init__ store the name, bases, mapping
* type.__getattr__ implement the dotted lookup "the dot"
* type.__call__ makes the instance
* type.__repr__ controls how the class display


instances:

* object.__metaclass___ = type 
* object.__getattr__      implements the dotted lookup 
* object.__repr__         controls how the instances display

'''

### Normal class

class Circle:
    'A roundish thing'
    
    __metaclass__  = type
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2.0

    
## Modify the repr

class CuteReprMetaclass(type):
    def __repr__(cls):
            return '<! %s !>' % cls.__name__

class Circle:
    'A roundish thing'

    __metaclass__ = CuteReprMetaclass

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2.0

    def __repr__(self):
        return 'Instance of %s' %self.__class__.__name__

## have the class track all instances

inst_list = []


class InstanceTrackingMetaclass(type):
    def __call__(self, *args):
        if inst_list:
            return inst_list[0]

        inst = type.__call__(self, *args)
        inst_list.append(inst)
        return (inst)
    
class Circle:
    'A roundish thing'

    __metaclass__ = InstanceTrackingMetaclass

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2.0

    def __repr__(self):
        return 'Instance of %s' %self.__class__.__name__


class SingletonMakeingMetaclass(type):
    def __call__(self, *args):
        if inst_list:
            inst_list[0].count +=  1
            return inst_list[0]

        inst = type.__call__(self, *args)
        inst.count = 1
        inst_list.append(inst)
        return (inst)
    
class Circle:
    'A roundish thing'

    __metaclass__ = SingletonMakeingMetaclass

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2.0

    def __repr__(self):
        return 'Instance of %s' %self.__class__.__name__

c = Circle (10)
d = Circle (20)


## Dynamic Lookup

from time import ctime
from random import randrange

class DynamicMeta(type):

    def __getattribute__(cls,attr):
        if attr == 'time':
            return ctime()

        if attr == 'roll':
            return randrange(6)
        
        result = type._-getattribute__(cls,attr)
        return result

class Circle:
    'A roundish thing'

    __metaclass__ = DynamicMeta

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2.0

    def __repr__(self):
        return 'Instance of %s' %self.__class__.__name__

### Override New ###


def  welcome(self):
    print 'Hello'

class NewMeta(type):
    def __new__(mcls, name, bases, mapping):
        name = 'Shape' + name
        mapping['welcome'] = welcome
        if 'attributes' in mapping:
            for attribute in mapping['attributes']:
                mapping[attribute] = 0

        return type.__new__(mcls, name, bases, mapping)

class Shape:
    __metaclass__ = NewMeta
    
class Circle(Shape):
    'A roundish thing'

    attributes = 'width', 'color', 'weight'
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2.0



class Square:
    'A sqarish thing'

    __metaclass__ = NewMeta

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2.0

    def __repr__(self):
        return 'Instance of %s' %self.__class__.__name__

c = Circle(10)
c = Circle(20)
e = Square(10)
