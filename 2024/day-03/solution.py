import re

def getData(input):
  f = open(input, 'r')
  return f.readlines()

def main(part):
  data = getData('2024\\day-03\\data\\input.txt')
  sum = 0
  enabled = True

  for line in data:
    parse = re.findall('mul\\((\\d+),(\\d+)\\)|(don\'t\\(\\))|(do\\(\\))', line)

    for pair in parse:
      if pair[2] != '':
        enabled = False
      elif pair[3] != '':
        enabled = True

      if pair[0] and pair[1] and (enabled or part == 1):
        sum += int(pair[0]) * int(pair[1])
  
  print("Part " + str(part) + ": " + str(sum))

main(1)
main(2)