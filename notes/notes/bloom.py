'Implement a BloomFilter from scratch'

from random import seed, sample

try:
    from cbitarray import BitArray
except ImportError:
    from bitarray import BitArray

try:
    import cPickle as pickle
except ImportError:
    import pickle

class Bloom:

    def __init__(self, pop=56, probes=6):
        self.pop = xrange(pop)
        self.probes = probes
        self.array = BitArray(pop)

    def add(self, element):
        seed(element)
        lucky = sample(self.pop, self.probes)
        for i in lucky:
            self.array[i] = 1

    def __contains__(self, element):
        seed(element)
        lucky = sample(self.pop, self.probes)
        return all(self.array[i] for i in lucky)

def make_checker(wordfile='notes/words.txt', cache_file='wordbits.pcl'):
    'Store a wordlist in a Bloom filter'
    try:
        with open(cache_file, 'rb') as f:
            return pickle.load(f)
    except IOError:
        pass

    wordlist = Bloom(pop=4000000, probes=12)
    with open(wordfile) as f:
        for line in f:
            word = line.rstrip()
            wordlist.add(word.lower())

    with open(cache_file, 'wb') as f:
        pickle.dump(wordlist, f, 2)

    return wordlist

def spellcheck(text, wordlist):
    'Show misspellings'
    for word in text.lower().split():
        if word not in wordlist:
            print word

if __name__ == '__main__':
    hettingers = Bloom()
    for name in 'raymond rachel matthew ramon sharon dennis gayle'.split():
        hettingers.add(name)

    text = '''
    Now iss the tyme for alll good mehn
    to coome to thhe aid of thur country

    Shee selz sea shells
    
    '''

    wordlist = make_checker()
    spellcheck(text, wordlist)

