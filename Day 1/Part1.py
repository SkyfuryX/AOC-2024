input = open('Day 1\\input.txt')
left = []
right = []
total = 0

for line in input:
    parts = line.split()
    left.append(int(parts[0]))
    right.append(int(parts[1]))

left.sort()
right.sort()

for i in range(len(left)):
    if left[i] > right[i]:
        total += left[i] - right[i]
    else:
        total += right[i] - left[i]

print(total)

input.close()