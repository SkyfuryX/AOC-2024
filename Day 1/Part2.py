input = open('Day 1\\input.txt')
left = []
right = []
similarity = 0

for line in input:
    parts = line.split()
    left.append(int(parts[0]))
    right.append(int(parts[1]))

for i in range(len(left)):
    similarity += left[i] * right.count(left[i])

print(similarity)
