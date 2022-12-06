def findMarker(signal, window):
    buffer, marker = '', 0
    for x, c in enumerate(signal):
        buffer += c
        if len(buffer) == window:
            if len(set(buffer)) == window:
                marker = x + 1
                break
            else:
                buffer = buffer[1:]
    return marker

f = open('2022\\day-06\\data\\input.txt', 'r')
data = f.readline()

print("part one:", findMarker(data, 4))
print("part two:", findMarker(data, 14))