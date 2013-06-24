counter = 0

class FieldDefinition(object):

    def __init__(self,size):
        global counter
        self.position = counter
        counter += 1
        self.size = size

class String(object):
    def __init__(self,size):
        global counter
        self.position = counter
        self.size = size
        counter += 1
        self.size = size

    def __set__(self, obj, value):
        print 'Setting', obj, 'to', value

class Int(FieldDefinition):

    def __init__(self,size):
        global counter
        self.position = counter
        counter += 1
        self.size = size


    def __set__(self, obj, value):
        print 'Creating SQL to setting', obj, 'to', value
        
class ModelMeta(type):
    def __new__(mcls, name,bases, mapping):
        field_defs = [ (k,v)  for k, v in mapping.items() if isinstance(v, FieldDefinition)]
        field_defs.sort(key=lambda(kv,v): v.position)
        print 'Creating a table with:'
        for k,v in field_defs:
            print k, v.__class__.__name__, v.size
            
        return type.__new__(mcls, name, bases, mapping)

class Model(object):
    __metaclass__ = ModelMeta


#############################
# from orm import Model


class Person(Model):
    versions = '0.1'
    name = String (20)
    age = Int(3)

    def __init__(self, name, age):
        self.name = name
        self.age = age
                

P = Person('Raymond', 0x30)
P.age = 0x31
