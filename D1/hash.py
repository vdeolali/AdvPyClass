# how to instrument python obj
# understand x == y implies hast (x) == hash (y)


class Int(int):
    def __cmp__(self, other):
        print '!'
        return cmp(int(self), int(other))

    def __hash__(self):
        print '#'
        return hash (int(self))

    
