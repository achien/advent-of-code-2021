import fileinput

depths = []
for line in fileinput.input():
    depths.append(int(line))

increases = 0
for i in range(len(depths) - 3):
    if sum(depths[i+1:i+4]) > sum(depths[i:i+3]):
        increases += 1

print(increases)