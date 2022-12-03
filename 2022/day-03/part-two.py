import string
lowerValues, upperValues = dict(), dict()
for index, letter in enumerate(string.ascii_lowercase):
   lowerValues[letter] = index + 1
for index, letter in enumerate(string.ascii_uppercase):
   upperValues[letter] = index + 27

try:
   from itertools import izip_longest
except ImportError:
    from itertools import zip_longest as izip_longest

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)

def findBadge(lines):
    sum = 0
    group = [lines[0].splitlines()[0], lines[1].splitlines()[0], lines[2].splitlines()[0]]
    badge = set.intersection(*map(set, group))

    if list(badge)[0].isupper():
        sum += upperValues[list(badge)[0]]
    else:
        sum += lowerValues[list(badge)[0]]
    return sum

with open('2022\\day-03\\data\\input.txt') as f:
    total = 0
    for elfGroup in grouper(f, 3, ''):
        assert len(elfGroup) == 3
        total += findBadge(elfGroup)

    print(total)