'''
* Storing the midpoint wastes space
* stored midpoint can become inconsistent
* API inconsistent: two attr and one
'''


class PriceRange(object):
    def __init__(self, low, high):
        self.low = low
        self.high = high

    @property
    def midpoint(self):
        return (self.low + self.high)/2.0

p = PriceRange(10,19)



class Demo(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add_parts(self):
        return self.a + self.b

    total = property(add_parts)


