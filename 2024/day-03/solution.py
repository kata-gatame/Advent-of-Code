import sys
sys.path.insert(1, "./2024/helpers")
import util as util
import re

def main(part):
  data = util.getData('03')
  parse = re.findall('mul\\((\\d+),(\\d+)\\)|(don\'t\\(\\))|(do\\(\\))', data)

  enabled = True
  sum = 0

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