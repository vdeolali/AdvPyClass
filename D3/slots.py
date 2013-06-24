

class Member(object):
    'Descriptor implementing slot lookup'

    def __init__(self,i):
        self.i = i

    def __get__(self,obj, type=None):
        return obj._slotvalues[self.i]

    def __set__(self, obj, value):
        obj._slotvalues[self.i] = value


class SlotMeta(type):
    def __new__(mcls, name, bases, mapping):
        if '_slot_':
            slots = mapping['_slots_']
            mapping['_slotvalue'] = [0] * len(slots)
            for i, slot in enumerate(slots):
                mapping[slot] = Member(i)
                
        return type.__new__(mcls, name, bases, mapping)
    


##########################

class A:

    __metaclass__ = SlotMeta
    
    _slots_  = 'a', 'b', 'c'

p = A()
q = A()


class B(object):

    __slots__ = 'a', 'b', 'c'

    
