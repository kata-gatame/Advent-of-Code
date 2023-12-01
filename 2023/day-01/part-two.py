def getData(input):
    f = open(input, 'r')
    return f.readlines()

def getSum(data):
    numberPhrases = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    sum = 0

    for line in data:
        first = ""
        last = ""
        for i, c in enumerate(line):
            if c.isdigit():
                if first == "":
                    first = c
                last = c
                continue

            for phrase in numberPhrases:
                if line[i:i + len(phrase)] == phrase:
                    if first == "":
                        first = numberPhrases.index(phrase) + 1
                    last = numberPhrases.index(phrase) + 1
        
        sum += int(f"{first}{last}")

    return sum

def main():
    data = getData('2023\\day-01\\data\\input-p2.txt')
    sum = getSum(data)

    print("Part Two - Calibration Values Sum: ", sum)

main()