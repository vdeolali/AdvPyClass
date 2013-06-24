def parse(data):
    'Parse a variable length record format'
    i = 0
    while i < len(data):
        kind = data[i]
        i += 1
        if 0:
            pass
        elif kind == 'p':
            lastname = str(data[i:i+8]).rstrip()
            i += 8
            age = int(data[i:i+4])
            i += 4
            print dict(kind=kind, lastname=lastname, age=age)
        elif kind == 'c':
            firstname = str(data[i:i+10]).rstrip()
            i += 10
            height = float(data[i:i+12])
            i += 12
            print dict(kind=kind, firstname=firstname, height=height)
        else:
            raise ValueError('Unknown kind: ' + kind)

if 0:
    sample_data = 'pSmith     15pJones      9cRaymond           63.7'
    parse(sample_data)


###########################################
####### Your Turn.    Class Exercise ######

# Hint 1:  cut-and-paste, then parameterize
# Hint 2:  use multi-line strings with a leading backslash
# Hint 3:  work from inside out
# Hint 4:  develop using print, then turn into a generator

header = '''\
def parse(data):
    'Parse a variable length record format'
    i = 0
    while i < len(data):
        kind = data[i]
        i += 1
        if 0:
            pass
'''

test_line = '''\
        elif kind == '%s':
'''

str_field = '''\
            %s = str(data[i:i+%d]).rstrip()
            i += %d
'''

reg_field = '''\
            %s = %s(data[i:i+%d])
            i += %d
'''

kind_line = '''\
            print dict(kind=kind, %s)
'''

footer = '''\
        else:
            raise ValueError('Unknown kind: ' + kind)
'''

record_type = 'a'
record_spec = [('hometown', str, 20), ('pop_density', float, 15), ('long', float, 8),
              ('lat', float, 4)]

def generate_parse_record_type(record_layout):
    yield header
    for record_type, record_spec in record_layout.items():
        yield test_line % record_type
        field_names = []
        for fname, ftype, fwidth in record_spec:
            field_names.append(fname)
            if ftype is str:
                yield str_field % (fname, fwidth, fwidth)
            else:
                yield reg_field % (fname, ftype.__name__, fwidth, fwidth)   
        pairs = ', '.join(['%s=%s' % (fname, fname) for fname in field_names])
        yield kind_line % pairs
    yield footer

def parse_record_type(record_layout, verbose=False):
    text = ''.join(generate_parse_record_type(record_layout))
    if verbose:
        print text
    d = {}
    exec text in globals(), d
    return d['parse']

###########################################
#######    Client Code               ######

if 1:

    record_layout = {
        'p': [('lastname', str, 8), ('age', int, 4)],
        'c': [('firstname', str, 10), ('height', float, 12)],
        'q': [('military_id', str, 14), ('blood_type', str, 1), ('rank', int, 2)],
        'a': [('hometown', str, 20), ('pop_density', float, 15), ('long', float, 8),
              ('lat', float, 4)],
    }
    parse = parse_record_type(record_layout, verbose=True)
    sample_data = 'pSmith     15pJones      9cRaymond           63.7'
    parse(sample_data)


