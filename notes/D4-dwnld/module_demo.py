'Show how import logic works'

import sys
import os

module_cache = {}                      # just like sys.modules

class Module(object):

    def __init__(self, mapping):
        self.mapping = mapping

    def __getattr__(self, attr):
        return self.mapping[attr]

def myimport(modname):
    if modname in module_cache:
        module = module_cache[modname]
        globals()[modname] = module
        return
    
    filename = modname + '.py'       # pyc  pyo  so  dll  zip

    for dirname in sys.path:
        fullname = os.path.join(dirname, filename)
        try:
            with open(fullname) as f:
                body = f.read()
            break
        except IOError:
            pass
    else:                            # no break
        raise ImportError(modname)

    namespace = {}
    namespace['__name__'] = modname
    namespace['__file__'] = fullname
    exec body in namespace
    module = Module(namespace)
    
    module_cache[modname] = module
    globals()[modname] = module
                 
def myreload(module):
    modname = module.__name__
    if modname in module_cache:
        del module_cache[modname]
    myimport(modname)
    return module_cache[modname]
    


if __name__ == '__main__':
    myimport('example')       # import example
    print example.x
    print example.square(5)

    myimport('random')
    print random.randrange(10)
