import string
lowerValues, upperValues = dict(), dict()
for index, letter in enumerate(string.ascii_lowercase):
   lowerValues[letter] = index + 1
for index, letter in enumerate(string.ascii_uppercase):
   upperValues[letter] = index + 27

f = open('2022\\day-03\\data\\input.txt', 'r')
data = f.readlines()
sum = 0

for line in data:
    compSize = len(line.strip()) // 2
    c1, c2 = set(line[:compSize]), set(line[compSize:])
    ci = ''.join(sorted(c1.intersection(c2)))

    if ci.isupper():
        sum += upperValues[ci]
    else:
        sum += lowerValues[ci]

print(sum)