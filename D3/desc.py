

class Desc(object):

    def __get__(self,obj, objtype):
        print 'Invoked'
        print 'Returning x + 10'
        return obj.x + 10




class A(object):

    def __init__(self,x):
        self.x = x


    plus_ten = Desc()
    

class B(object):

    def __init__(self,x):
        self.x = x
        self.plus_ten = Desc()
        

def square(x):
    return x*x

def f(*args):
    print "called with ", args
    return 42

# f(10,20,30) invokes f.__call__(10,20,30)
# b.f  becomes b.__class__.__dict_-['f].__get__(b, A)

class BoundMethod:
    def __init__(self,func, inst):
        self.func = func
        self.inst = inst

    def __call__(self,*args):
        return self.func(self.inst, *args)

class C:
    def bark(self,x):
        print 'Barking with', x

"""

Functions has __get__
   So if you put them in a class, a.f -->   a.__class__.__dict__['f'].__get__
   The output is a boundmethod
   the net effect is SELF is prepended to the function call


   Staticmethods wrap functions.
   They have a __get__ method
   so if you put them in a class, a.f   --

"""


