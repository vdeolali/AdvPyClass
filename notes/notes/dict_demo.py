'Develop advanced skills with dictionaries'

# Dict constructors

d = {'raymond': 'red', 'rachel': 'blue'}   # literal notation uses curly braces and colons

d = dict([('raymond', 'red'),              # list of tuples
          ('rachel', 'blue')])

d = dict(raymond='red', rachel='blue')     # keyword args don't need quotes

########################################
# dict.fromkeys(seq)

names = 'raymond rachel matthew'.split()
d = dict.fromkeys(names, '<unspecified>')

#######################################
# d[k] looks up k and returns the values
# if k is not found, it calls d.__missing__(k)
# the default behavior of __missing is to raise a KeyError
# A super-power of dictionaries is the ability to override this

class AngryDict(dict):
    def __missing__(self, key):
        print 'Argh!  I am really angry that', key, 'is missing'
        raise KeyError(key)

ad = AngryDict()

## Counting example #######################

class ZeroDict(dict):
    def __missing__(self, key):
        return 0

zd = ZeroDict()
for color in 'red green red blue green red'.split():
    zd[color] += 1
print zd

## Grouping examples #######################
# Pattern d[group] = [list of things in that group]

class ListDict(dict):
    'Useful for grouping'
    def __missing__(self, key):
        self[key] = []
        return self[key]

names = 'mary brian sam linda julie jenny betty'.split()

# Grouping by the length of the name
d = ListDict()
for name in names:
    key = len(name)
    d[key].append(name)
print d
    
# Group by the first character of the name
d = ListDict()
for name in names:
    key = name[0]
    d[key].append(name)
print d

# Group by the last character of the name
d = ListDict()
for name in names:
    key = name[-1]
    d[key].append(name)
print d

# Group by the number of vowels in the name
d = ListDict()
for name in names:
    key = sum(name.count(vowel) for vowel in 'aeiouy')
    d[key].append(name)
print d

## String substitution example #####################

class DefaultFormatDict(dict):
    'Provide support for multi-pass substitution'
    def __missing__(self, key):
        return '%(' + key + ')s'

d = DefaultFormatDict(name='Rachel')

print 'Good morning %(title)s %(name)s!' % d
print 'Good morning %(title)s %(name)s!' % d % dict(title='Mrs.')

## Linked dictionary ################################

class ChainDict(dict):
    def __init__(self, secondary):
        self.secondary = secondary
    def __missing__(self, key):
        return self.secondary[key]

default_colors = dict(foreground='white', background='cyan')
cd = ChainDict(default_colors)
cd['foreground'] = 'grey'
print cd['foreground']
print cd['background']

