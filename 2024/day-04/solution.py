import sys
sys.path.insert(1, './2024/helpers')
import util
import numpy as np

def main(part):
  field = util.getDataMatrix('04')
  count = 0

  if part == 1:
    for _ in range(4):
      field = np.rot90(field)
      count += sum([''.join(line).count('XMAS') for line in field])

    for _ in range(4):
      field = np.rot90(field)
      count += sum([''.join(np.diagonal(field, x)).count('XMAS') for x in range(len(field) - 3)])
      count += sum([''.join(np.diagonal(field, x + 1, 1, 0)).count('XMAS') for x in range(len(field) - 3)])

  if part == 2:
    for x in range(len(field) - 2):
      for y in range(len(field) - 2):
        window = field[x:x + 3, y:y + 3]

        for _ in range(4):
          window = np.rot90(window)
          d1 = ''.join(np.diagonal(window))
          d2 = ''.join(np.diagonal(np.rot90(window)))

          if d1 == 'MAS' and d2 == 'MAS':
            count += 1

  print(f'Part {part}: {count}')
main(1)
main(2)