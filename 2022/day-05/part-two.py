import re

f = open('2022\\day-05\\data\\input.txt', 'r')
data = f.readlines()
regex = re.compile('^move (\d+) from (\d+) to (\d+)$')
stacks = [ [] for _ in range(35) ]

def build():
    for line in data:
        locations = [i for i in range(len(line)) if line[i].isupper()]
        for l in locations:
            stacks[l].append(line[l])
        if line == '\n':
            break
    return [x for x in stacks if x]

def move(warehouse):
    for line in data:
        matches = re.search(regex, line)
        if matches:
            a, s, d, x, temp = int(matches.group(1)), int(matches.group(2)), int(matches.group(3)), 1, []
            while x <= a:
                if warehouse[s-1]:
                    crate = warehouse[s-1].pop(0)
                    temp.insert(0, crate)
                x += 1

            temp.reverse()
            temp.extend(warehouse[d-1])
            warehouse[d-1] = temp

def giveMeTheAnswer(w):
    ans = ''
    for l in w:
        ans += l[0]
    print(ans)

w = build()
move(w)
giveMeTheAnswer(w)