import collections

print 'Regular dictionary:'

d = {'a': 'A', 'b': 'B','c': 'C'}

for k,v in d.items():
    print k,v


print'\nOrderedDict:'

d = collections.OrderedDict()

d['a']='A'
d['b']='B'
d['c']='C'

for k,v in d.items():
    print k,v

print 'dic   :'
d1 = {}
d1['a']='A'
d1['b']='B'
d1['c']='C'

d2={}
d2['c']='C'
d2['b']='B'
d2['a']='A'

print d1==d2

print 'OrderedDict:  '


d1 = collections.OrderedDict()
d1['a']='A'
d1['b']='B'
d1['c']='C'

d2 = collections.OrderedDict()
d2['c']='C'
d2['b']='B'
d2['a']='A'

print d1==d2