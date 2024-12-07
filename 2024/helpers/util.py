import numpy as np

def getData(input):
  f = open(f'2024\\day-{input}\\data\\input.txt', 'r')
  return f.read()

def getDataByLine(input):
  f = open(f'2024\\day-{input}\\data\\input.txt', 'r')
  return f.readlines()

def getDataMatrix(input):
  f = open(f'2024\\day-{input}\\data\\input.txt', 'r')
  return np.array([np.array(list(line.strip())) for line in f.readlines()])