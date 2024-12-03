import sys
sys.path.insert(1, "./2024/helpers")
import util as util

def main(part):
  data = util.getData('00')
  sum = 0

  print("Part " + str(part) + ": " + str(sum))

main(1)
main(2)