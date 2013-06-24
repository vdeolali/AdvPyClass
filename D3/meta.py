from pprint import pprint


# what the CLASS keyword does
# execs the code and creates a dictionary: mapping
# mc = mapping['__metaclass__']
# Dog = mc('Dog', (), mapping)
# adds '__module__' to the dictionary



def explore(*args):
    'called with:'
    pprint (args)
    return 42

class Dog:
    __metaclass__ = explore
    x = 1
    def bark(self):
        pass

def makedict (name, bases, mapping):
    return mapping

class d:
    __metaclass__  = makedict
    raymond = 'red'
    rachel  = 'blue'
    matthew  = 'green' 
   
