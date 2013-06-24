'Implement a Bloomfilter from scratch'

from random import *
import pickle
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

def make_checker(wordfile='words.txt', cache_file='words.pcl'):
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

def spellcheck (text, wordlist):
    'Show misspellings'
    for word in text.lower().split():
        if word not in wordlist:
            print word
            
if __name__ == '__main__':
    bf = Bloom()
    for name in 'raymond rachel matthew ramon, sharon'.split():
        bf.add(name)


    text = '''
    Now iss the tyme for all good mehn to coome to thhe aid fo thur country
    '''

    wordlist = make_checker()
    spellcheck(text, wordlist)
