<<<<<<< HEAD
import re

r = open('Day 3\\input.txt', "r")
input = r.read() 
 
results = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", input)
total = 0
do = True

for item in results:
    if item == "don't()":
        do = False
    elif item == 'do()':
        do = True
 
    if do == True and item[0:3] == 'mul':
        step = item.replace('mul(','').replace(',',' ').replace(')','')
        step = step.split()
        total += int(step[0]) * int(step[1])

=======
import re

r = open('Day 3\\input.txt', "r")
input = r.read() 
 
results = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", input)
total = 0
do = True

for item in results:
    if item == "don't()":
        do = False
    elif item == 'do()':
        do = True
 
    if do == True and item[0:3] == 'mul':
        step = item.replace('mul(','').replace(',',' ').replace(')','')
        step = step.split()
        total += int(step[0]) * int(step[1])

>>>>>>> 3c9ece336fadd22a7c1468a76f66d6ad395f0fa7
print(total) 