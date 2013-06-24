'Show how import logic works'
import sys
import os


class Module(object):
    def __init__(self, mapping):
        self.mapping = mapping

    def __getattr__(self,attr):
        return self.mapping[attr]


def myimport(modname):

    if modname in module_cache:
        module = module_cache[modname]
        globals()[modname] = module
        return
    
    filename = modname +'.py'

    for dirname in sys.path:
        fullname = os.path.join(dirname, filename)
        try:
            with open(fullname) as f:
                body = f.read()
            break

        except IOError:
            pass

    else:
        raise ImportError(modname)

    namespace = {}
    namespace['__file__'] = filename
    namespace['__name__'] = modname
    exec body in namespace
    module = Module(namespace)
    module_cache[modname] = module
    globals()[modname] =  module


module_cache = {}

def myreload(module):
    modname = module.__name__
    if modname in module_cache:
        del module_cache[modname]
    myimport(modname)
    return module_cache[modname]

if __name__ == '__main__':
    myimport ('example')    # import example
    print example.x
    print example.square(5)
    
