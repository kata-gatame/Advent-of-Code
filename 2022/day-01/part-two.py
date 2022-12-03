# f = open('2022\\day-01\\data\\test-data.txt', 'r')
f = open('2022\\day-01\\data\\input.txt', 'r')

data = f.readlines()

sum = 0
cls = []

for line in data:
    if line.splitlines()[0].isdigit():
        sum += int(line.splitlines()[0])
    else:
        cls.append(sum)
        sum = 0

cls.sort(reverse=True)
sum = cls[0] + cls[1] + cls[2]

print("top 3 summed calories: ", sum)