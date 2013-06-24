'''
* storing the midpoint wastes space
* stored midpoint can become inconsistent
* API inconsistent:  two attributes and one method

'''


class PriceRange(object):

    def __init__(self, low, high):
        self.low = low
        self.high = high

    @property
    def midpoint(self):
        return (self.low + self.high) / 2.0

p = PriceRange(10, 19)
