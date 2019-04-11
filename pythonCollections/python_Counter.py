from collections import Counter
import re

# Find the top 5 most common letters in the samplestring
sampleString = 'jhnruinflkwmviojenoignerongiurheonenkoneoinvon7483u85u23095io4ut483jiqu34nf984hfouncu9n834fh7nu432fjldknxcvbnmdfghjertyu'
c = Counter()
for char in sampleString:
    c[char] += 1
print(c.most_common(5))

# Find top 5 most common numbers in sample string
pattern = '\D'
newString = re.sub(pattern, '', sampleString)
digitCounter = Counter()
for char in newString:
    digitCounter[char] += 1
print(digitCounter.most_common(5))
