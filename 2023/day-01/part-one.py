def getData(input):
    f = open(input, 'r')
    return f.readlines()

def getSum(data):
    sum = 0
    first = 0
    last = 0

    for line in data:
        for i, c in enumerate(line):
            if c.isdigit():
                last = c

        for i, c in enumerate(line[::-1]):
            if c.isdigit():
                first = c

        sum += int(first + last)
    return sum

def main():
    data = getData('2023\\day-01\\data\\input.txt')
    sum = getSum(data)
    
    print("Part One - Calibration Values Sum: ", sum)

main()