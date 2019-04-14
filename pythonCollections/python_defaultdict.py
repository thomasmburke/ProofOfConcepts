from collections import defaultdict

# Defaultdict give a default type to each of the keys values

#s = 'supercalifragilisticexpialidocious'
s = [{'yellow': 4}, {'orange': 8}, {'yellow': 6}]
d = defaultdict(list) # all values will be added in the form of a list
for color in s:
    for k,v in color.items():
        d[k].append(v)
#print(dict(d))


newDict = defaultdict(dict)
newDict['a']['b'] = 1
print(newDict)

import collections
# floyd warshall Algorithm
def calcEquation(equations, values, queries):
    quot = collections.defaultdict(dict)
    for (num, den), val in zip(equations, values):
        quot[num][num] = 1.0
        quot[den][den] = 1.0
        quot[num][den] = val
        quot[den][num] = 1 / val
    print(quot) # defaultdict(<class 'dict'>, {'a': {'a': 1.0, 'b': 2.0}, 'b': {'b': 1.0, 'a': 0.5, 'c': 3.0}, 'c': {'c': 1.0, 'b': 0.3333333333333333}})
    for k in quot:
        for i in quot[k]:
            for j in quot[k]:
                quot[i][j] = quot[i][k] * quot[k][j]
    print(quot) #defaultdict(<class 'dict'>, {'a': {'a': 1.0, 'b': 2.0, 'c': 6.0}, 'b': {'b': 1.0, 'a': 0.5, 'c': 3.0}, 'c': {'c': 1.0, 'b': 0.3333333333333333, 'a': 0.16666666666666666}})
    return [quot[num].get(den, -1.0) for num, den in queries]

equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]

print(calcEquation(equations, values, queries))
