import fileinput

h = 0
d = 0
a = 0
for line in fileinput.input():
    tokens = line.split()
    dir = tokens[0]
    n = int(tokens[1])
    if dir == 'forward':
        h += n
        d += a * n
    elif dir == 'down':
        a += n
    elif dir == 'up':
        a -= n

print(h * d)