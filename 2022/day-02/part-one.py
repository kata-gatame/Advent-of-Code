# f = open('2022\\day-02\\test-data.txt', 'r')
f = open('2022\\day-02\\input.txt', 'r')

data = f.readlines()

w = 6
d = 3
l = 0
score = 0

for line in data:
    round = line.split()
    o = round[0]
    s = round[1]

    match o:
        # rock
        case "A":
            match s:
                # rock
                case "X":
                    score += 1 + d
                
                # paper
                case "Y":
                    score += 2 + w
                
                # scissors
                case "Z":
                    score += 3 + l
        
        # paper
        case "B":
            match s:
                # rock
                case "X":
                    score += 1 + l
                
                # paper
                case "Y":
                    score += 2 + d
                
                # scissors
                case "Z":
                    score += 3 + w
        
        # scissors
        case "C":
            match s:
                # rock
                case "X":
                    score += 1 + w
                
                # paper
                case "Y":
                    score += 2 + l
                
                # scissors
                case "Z":
                    score += 3 + d

print(score)   
