from collections import OrderedDict

d = OrderedDict()
d['apple'] = 3
d['banana'] = 2
d['pear'] = 44
d['citrus'] = 7
print(d)
print('popping item..')
# default for popitem is LIFO
print(d.popitem())
print(d)
# We can change popitem to FIFO if last is set to false
print(d.popitem(last=False))
print(d)

d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
# dictionary sorted by key
d2 = OrderedDict(sorted(d.items(), key=lambda t: t[0]))

# dictionary sorted by value
d3 = OrderedDict(sorted(d.items(), key=lambda t: t[1]))

# dictionary sorted by length of the key string
d4 = OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
print(d)
print('sorted by key...')
print(d2)
print('sorted by value...')
print(d3)
print('sorted by key string length')
print(d4)
