def dotproduct(s, t):
    result = 0
    for i in range(min(len(s), len(t))):
        result += s[i] * t[i]
    return result

def manydots(n):
    return sum(dotproduct(xrange(n), xrange(i, i+n)) for i in range(n))

if __name__ == '__main__':
    import sys

    n = 10000
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    print manydots(n)
