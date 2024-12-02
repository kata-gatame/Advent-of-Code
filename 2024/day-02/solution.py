import math

def getData(input):
  f = open(input, 'r')
  return f.readlines()

def dampen(report):
  differences = [report[i] - report[i + 1] for i in range(len(report) - 1)]
  within_range = all([1 <= abs(d) <= 3 for d in differences])
  same_direction = all([math.copysign(1, d) == math.copysign(1, differences[0]) for d in differences])
  return within_range and same_direction

def main():
  data = getData('2024\\day-02\\data\\input.txt')
  reports = [[int(i) for i in line.split()] for line in data]

  safe_reports = 0
  safe_reports_dampened = 0

  for report in reports:
    safe = dampen(report)

    if safe:
      safe_reports += 1
      safe_reports_dampened += 1
    else:
      for i in range(len(report)):
        copy = report.copy()
        copy.pop(i)
        if dampen(copy):
          safe_reports_dampened += 1
          break

  print("Part 1: " + str(safe_reports))
  print("Part 2: " + str(safe_reports_dampened))

main()