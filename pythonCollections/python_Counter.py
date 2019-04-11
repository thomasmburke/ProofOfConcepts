from collections import Counter

# Find the top 5 most common letters in the samplestring
sampleString = 'jhnruinflkwmviojenoignerongiurheonenkoneoinvon7483u85u23095io4ut483jiqu34nf984hfouncu9n834fh7nu432fjldknxcvbnmdfghjertyu'
c = Counter()
for char in sampleString:
    c[char] += 1
print(c.most_common(5))
