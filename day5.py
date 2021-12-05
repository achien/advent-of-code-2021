import fileinput

counts = {}
for line in fileinput.input():
    line = line.strip()
    p1, p2 = line.split('>')
    p1 = p1[:-2]
    x1, y1 = p1.split(',')
    x1 = int(x1)
    y1 = int(y1)

    p2 = p2[1:]
    x2, y2 = p2.split(',')
    x2 = int(x2)
    y2 = int(y2)

    if x1 == x2:
        dx = 0
    elif x1 > x2:
        dx = -1
    else:
        dx = 1
    if y1 == y2:
        dy = 0
    elif y1 > y2:
        dy = -1
    else:
        dy = 1

    x = x1
    y = y1
    while True:
        pt = (x, y)
        counts[pt] = counts.get(pt, 0) + 1
        if x == x2 and y == y2:
            break
        x += dx
        y += dy

n = 0
for _, ct in counts.items():
    if ct > 1:
        n += 1
    
print(n)