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
    total = 0

    for game in data:
        redCubes = []
        greenCubes = []
        blueCubes = []
        
        minRed = 0
        minGreen = 0
        minBlue = 0

        start = game.index(': ')
        end = len(game)
        rounds = game[start+1:end].lstrip().rstrip('\n').split('; ')
        
        for round in rounds:
            reds = [int(s) for s in re.findall(r"(\d+)\sred", round)]
            greens = [int(s) for s in re.findall(r"(\d+)\sgreen", round)]
            blues = [int(s) for s in re.findall(r"(\d+)\sblue", round)]
            
            if (reds):
                redCubes.append(int(reds[0]))
                minRed = max(minRed, int(reds[0]))
            if (greens):
                greenCubes.append(int(greens[0]))
                minGreen = max(minGreen, int(greens[0]))
            if (blues):
                blueCubes.append(int(blues[0]))
                minBlue = max(minBlue, int(blues[0]))

        total += (minRed * minGreen * minBlue)

    return total

def main():
    data = getData('2023\\day-02\\data\\input.txt')
    amt = processGame(data)
    
    print("Part Two - Game Power Sum: ", amt)

main()