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
