f = open('2022\\day-04\\data\\input.txt', 'r')
data = f.readlines()

m = 0
for line in data:
    oneStart, oneEnd = line.splitlines()[0].split(",")[0].split("-")
    twoStart, twoEnd = line.splitlines()[0].split(",")[1].split("-")

    if int(oneStart) <= int(twoEnd) and int(twoStart) <= int(oneEnd):
        m += 1

print(m)