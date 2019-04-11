from collections import Counter
import re

# Find the top 5 most common letters in the samplestring
sampleString = 'jhnruinflkwmviojenoignerongiurheonenkoneoinvon7483u85u23095io4ut483jiqu34nf984hfouncu9n834fh7nu432fjldknxcvbnmdfghjertyu'
c = Counter()
#for char in sampleString:
#    c[char] += 1
c.update(sampleString)
print(c.most_common(5))

# Find top 5 most common numbers in sample string
pattern = '\D'
newString = re.sub(pattern, '', sampleString)
digitCounter = Counter()
#for char in newString:
#    digitCounter[char] += 1
digitCounter.update(newString)
print(digitCounter.most_common(5))

# NOTE: the update function can be used with a string, list, or dict
myList = ['r','4']
digitCounter.update(myList)

mostCommonDigit = digitCounter.most_common(1)
print('mostCommonDigit = {}'.format(mostCommonDigit[0][0]))
print('mostCommonDigit Frequency = {}'.format(mostCommonDigit[0][1]))
print('digitCounter dict = {}'.format(dict(digitCounter)))
topDigitList = [x[0] for x in digitCounter]
print(mostCommonDigit)
print('topDigitList = {}'.format(topDigitList))

# Counter Arithmetic
c1 = Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = Counter('alphabet')

print('C1:', c1)
print('C2:', c2)

print('\nCombined counts:')
print(c1 + c2)

print('\nSubtraction:')
print(c1 - c2)

print('\nIntersection (taking positive minimums):')
print(c1 & c2)

print('\nUnion (taking maximums):')
print(c1 | c2)
