def getData(input):
  f = open(f'2024\\day-{input}\\data\\input.txt', 'r')
  return f.read()

def getDataByLine(input):
  f = open(f'2024\\day-{input}\\data\\input.txt', 'r')
  return f.readlines()