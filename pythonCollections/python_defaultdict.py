from collections import defaultdict

# Defaultdict give a default type to each of the keys values

#s = 'supercalifragilisticexpialidocious'
s = [{'yellow': 4}, {'orange': 8}, {'yellow': 6}]
d = defaultdict(list) # all values will be added in the form of a list
for color in s:
    for k,v in color.items():
        d[k].append(v)
print(dict(d))
