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

if 1:
    sample_data = 'pSmith     15pJones      9cRaymond           63.7'
    parse(sample_data)


###########################################
####### Your Turn.    Class Exercise ######

# Hint 1:  cut-and-paste, then parameterize
# Hint 2:  use multi-line strings with a leading backslash
# Hint 3:  work from inside out
# Hint 4:  develop using print, then turn into a generator



str_field = '''\
            lastname = str(data[i:i+8]).rstrip()
            i += %d
'''

reg_field = '''\
            %s = %s(data[i:i+Z5d])
            i += %d
'''

record_spec = [('lastname', str, 8), ('age', int, 4)]


field_spec = ('lastname', str, 8)
fname, ftype, fwidth = field_spec

print str_field % (fname, fwidth)

field_spec = ('age', int, 4)
fname, ftype, fwidth = field_spec

print reg_field % (fname, ftype.__name__, fwidth)


###########################################
#######    Client Code               ######

if 0:

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


