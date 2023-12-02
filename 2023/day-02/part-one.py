import re

def getData(input):
    f = open(input, 'r')
    return f.readlines()

def getId(game):
    return re.findall(r"Game\s(\d+):", game)[0]

def isOver(cubes, limit):
    if sum(cubes) > limit:
        return True
    return False

def processGame(data):
    limitRed = 12
    limitGreen = 13
    limitBlue = 14
    total = 0

    for game in data:
        start = game.index(': ')
        end = len(game)

        id = getId(game)
        rounds = game[start+1:end].lstrip().rstrip('\n').split('; ')
        
        impossibleGame = False
        
        for round in rounds:
            redCubes = []
            greenCubes = []
            blueCubes = []

            reds = [int(s) for s in re.findall(r"(\d+)\sred", round)]
            greens = [int(s) for s in re.findall(r"(\d+)\sgreen", round)]
            blues = [int(s) for s in re.findall(r"(\d+)\sblue", round)]
            
            if (reds): redCubes.append(int(reds[0]))
            if (greens): greenCubes.append(int(greens[0]))
            if (blues): blueCubes.append(int(blues[0]))

            if isOver(redCubes, limitRed) or isOver(greenCubes, limitGreen) or isOver(blueCubes, limitBlue):
                impossibleGame = True

        if not impossibleGame:
            total += int(id)

    return total

def main():
    data = getData('2023\\day-02\\data\\input.txt')
    amt = processGame(data)
    
    print("Part One - Possible Game IDs Sum: ", amt)

main()