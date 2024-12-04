import re

r = open('Day 3\\input.txt', "r")
input = r.read() 
 
results = re.findall('mul\(\d+,\d+\)', input)
total = 0

for item in results:
    item = item.replace('mul(','').replace(',',' ').replace(')','')
    item = item.split()
    total += int(item[0]) * int(item[1])
 
print(total) 