input = open('Day 2\\input.txt')
good = 0

for line in input:
    line = line.split()
    diff = 0
    safe = True
    if int(line[0]) == int(line[1]):
        safe = False
    elif int(line[0]) > int(line[1]):
        for i in range(len(line)-1):
            if int(line[i]) <= int(line[i+1]):
                safe = False
            diff = int(line[i]) - int(line[i+1])
            if not 0 < diff < 4:
                safe = False
    elif int(line[0]) < int(line[1]):
        for i in range(len(line)-1):
            if int(line[i]) >= int(line[i+1]):
                safe = False
            diff = int(line[i+1]) - int(line[i])
            if not 0 < diff < 4:
                safe = False

    print(' '.join(line) + ' ' + str(safe))
    if safe == True:
        good += 1

print(good)
