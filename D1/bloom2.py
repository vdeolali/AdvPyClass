'Implement a Bloomfilter from scratch'

from random import *

class Bloom:
    def __init__(self, pop=56, probes=6):
        self.pop = xrange(pop)
        self.probes = probes
        self.array = [0] * pop

    def add(self, element):
        seed(element)
        lucky = sample(self.pop, self.probes)
        for i in lucky:
            self.array[i] =1

    def __contains__(self, element):
        seed (element)
        lucky = sample (self.pop, self.probes)
        for i in lucky:
            if not self.array[i]:
                return False
        return True
    

if __name__ == '__main__':
    bf = Bloom()
    for name in 'raymond rachel matthew ramon, sharon'.split():
        bf.add(name)
        
