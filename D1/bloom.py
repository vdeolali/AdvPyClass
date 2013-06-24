'Implement a Bloomfilter from scratch'

from random import *

class Bloom:
    def __init__(self, pop=56, probes=6):
        self.pop = xrange(pop)
        self.probes = probes
        self.combined = set()

    def add(self, element):
        seed(element)
        lucky = sample(self.pop, self.probes)
        self.combined.update(lucky)

    def __contains__(self, element):
        seed (element)
        lucky = sample (self.pop, self.probes)
        return set(lucky) <= self.combined
    

if __name__ == '__main__':
    bf = Bloom()
    for name in 'raymond rachel matthew ramon, sharon'.split():
        bf.add(name)
        
