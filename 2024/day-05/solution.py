import sys
sys.path.insert(1, "./2024/helpers")
import util
from itertools import permutations

def getSumOfMiddles(updates):
  sum = 0
  for update in updates:
    i = int((len(update) - 1) / 2)
    sum += int(update[i])
  return sum

def reorderUpdate(update):
  # magical reorder
  return update

def main(part):
  data = util.getDataByLine('05')
  sum, rules, updates, valid, invalid, invalid_ro  = 0, [], [], [], [], []
 
  for line in data:
    if line.strip().find('|') > 0:
      rules.insert(1, line.strip().split('|'))
    elif line.strip().find(',') > 0:
      updates.insert(1, line.strip().split(','))

  rules = sorted(rules)

  for update in updates:
    isValid = True
    for x in range(len(update)):
      if x + 1 < len(update) and isValid:
        isValid = False if [update[x], update[x + 1]] not in rules else True
    if isValid:
      valid.insert(1, update)
    else:
      perms = set(permutations(update))
      for p in perms:
        isValid = True
        if x + 1 < len(p):
          for x in range(len(p)):
            isValid = False if [p[x], p[x + 1]] not in rules else True
        if isValid:
          invalid_ro.insert(1, p)
          break

  if part == 1:
    sum = getSumOfMiddles(valid)

  if part == 2:
    sum = getSumOfMiddles(invalid_ro)

  print(f'Part {part}: {sum}')
main(1)
main(2)