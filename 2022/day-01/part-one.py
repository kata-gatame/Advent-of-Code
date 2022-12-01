# f = open('2022\\day-01\\test-data.txt', 'r')
f = open('2022\\day-01\\input.txt', 'r')

data = f.readlines()

sum = 0
cls = 0

for line in data:
    if line.splitlines()[0].isdigit():
        cls += int(line.splitlines()[0])
        if cls > sum:
            sum = cls
    else:
        cls = 0

print("total calories: ", sum)