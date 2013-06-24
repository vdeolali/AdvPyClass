

counter = 0

class FieldDefinition(object):

    def __init__(self, size):
        global counter
        self.position = counter
        counter += 1
        self.size = size

class String(FieldDefinition):

    def __set__(self, obj, value):
        print 'Creating SQL to set', obj, 'to', value


class Int(FieldDefinition):

    def __set__(self, obj, value):
        print 'Creating SQL to set', obj, 'to', value

class ModelMeta(type):
    def __new__(mcls, name, bases, mapping):
        field_defs = [(k, v) for k, v in mapping.items() if isinstance(v, FieldDefinition)]
        field_defs.sort(key=lambda (k, v): v.position)
        print 'Creating a table with:'
        for k, v in field_defs:
            print k, v.__class__.__name__, v.size        
        return type.__new__(mcls, name, bases, mapping)

class Model(object):
    __metaclass__ = ModelMeta

######################################
#from orm import Model, String, Int

class Person(Model):
    versions = '0.1'

    name = String(20)
    age = Int(3)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person('Raymond', 0x30)
p.age = 0x31



