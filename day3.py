import fileinput

bits = []
for line in fileinput.input():
    line = line.strip()
    bits.append(line)

# gammas = ''
# epsilons = ''
# gamma = 0
# epsilon = 0
# for i in range(len(bits[0].strip())):
#     ones = 0
#     zeros = 0
#     for b in bits:
#         if b[i] == '0':
#             zeros += 1
#         else:
#             ones += 1
#     gamma *= 2
#     epsilon *= 2
#     if ones > zeros:
#         gamma += 1
#         gammas += '1'
#         epsilons += '0'
#     else:
#         epsilon += 1
#         gammas += '0'
#         epsilons += '1'
print()
print()
print()
width = len(bits[0])
o2nums = list(bits)
for i in range(width):
    ones = 0
    zeros = 0
    for b in o2nums:
        if b[i] == '0':
            zeros += 1
        else:
            ones += 1
    if ones >= zeros:
        o2nums = [n for n in o2nums if n[i] == '1']
    else:
        o2nums = [n for n in o2nums if n[i] == '0']
    if len(o2nums) == 1:
        o2num = o2nums[0]
        print(o2num)
        break


co2nums = list(bits)
for i in range(width):
    ones = 0
    zeros = 0
    for b in co2nums:
        if b[i] == '0':
            zeros += 1
        else:
            ones += 1
    if ones < zeros:
        co2nums = [n for n in co2nums if n[i] == '1']
    else:
        co2nums = [n for n in co2nums if n[i] == '0']
    if len(co2nums) == 1:
        co2num = co2nums[0]
        print(co2num)
        break

o2 = 0
for b in o2num:
    o2 *= 2
    o2 += int(b)

co2 = 0
for b in co2num:
    co2 *= 2
    co2 += int(b)

print(o2, co2)
print(o2 * co2)