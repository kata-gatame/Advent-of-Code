import re

list_a = []
list_b = []

def getData(input):
    f = open(input, 'r')
    return f.readlines()

def getLists(data):
    for line in data:
        parse = re.search('(\\d+)\\s{3}(\\d+)', line)
        list_a.append(parse.group(1))
        list_b.append(parse.group(2))

def main(part):
    data = getData('2024\\day-01\\data\\input.txt')    
    getLists(data)
    sum = 0

    if (part == 1):
        s1 = sorted(list_a)
        s2 = sorted(list_b)
        for x in range(len(list_a)):
            left = int(s1[x])
            right = int(s2[x])
            if left > right:
                sum += left - right
            else:
                sum += right - left

    if (part == 2):
        for x in list_a:
            left = int(x)
            sum += left * list_b.count(str(left))

    print("Part " + str(part) + ": " + str(sum))

main(1)
main(2)