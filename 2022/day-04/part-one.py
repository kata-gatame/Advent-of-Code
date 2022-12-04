f = open('2022\\day-04\\data\\input.txt', 'r')
data = f.readlines()

m = 0
for line in data:
    oneStart, oneEnd = line.splitlines()[0].split(",")[0].split("-")
    twoStart, twoEnd = line.splitlines()[0].split(",")[1].split("-")

    if int(oneStart) <= int(twoStart) and int(oneEnd) >= int(twoEnd):
        m += 1
    elif int(twoStart) <= int(oneStart) and int(twoEnd) >= int(oneEnd):
        m += 1

print(m)