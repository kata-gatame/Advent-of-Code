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
                # lose
                case "X":
                    score += 3 + l
                
                # draw
                case "Y":
                    score += 1 + d
                
                # win
                case "Z":
                    score += 2 + w
        
        # paper
        case "B":
            match s:
                # lose
                case "X":
                    score += 1 + l
                
                # draw
                case "Y":
                    score += 2 + d
                
                # win
                case "Z":
                    score += 3 + w
        
        # scissors
        case "C":
            match s:
                # lose
                case "X":
                    score += 2 + l
                
                # draw
                case "Y":
                    score += 3 + d
                
                # win
                case "Z":
                    score += 1 + w

print(score)
