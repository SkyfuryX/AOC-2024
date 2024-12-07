with open('Day 4\\input.txt') as r:
    input = r.readlines()

total = 0

#check to make sure indexes would not overflow to end of line/list
def valid_both(num, i):
    if num-3 < 0 or i-3 < 0:
        return False
    else:
        return True

def valid_i(i):
    if i-3 < 0:
        return False
    else:
        return True
    
def valid_num(num):
    if num-3 < 0:
        return False
    else:
        return True

for num, line in enumerate(input):
    for i in range(len(line.strip())):
        if input[num][i] == 'X':
            try: 
                if input[num][i+1] + input[num][i+2] + input[num][i+3] == 'MAS': #right
                    total +=1                         
            except IndexError:
                pass
            try:
                if valid_i(i) is True:
                    if input[num][i-1] + input[num][i-2] + input[num][i-3] == 'MAS': #left
                        total +=1 
            except IndexError:
                pass
            try:            
                if input[num+1][i] + input[num+2][i] + input[num+3][i] == 'MAS': #down
                    total +=1                    
            except IndexError:
                pass
            try:
                if valid_num(num) is True:
                    if input[num-1][i] + input[num-2][i] + input[num-3][i] == 'MAS': #up
                        total +=1                          
            except IndexError:
                pass
            try:
                if valid_both(num, i) is True:
                    if input[num-1][i-1] + input[num-2][i-2] + input[num-3][i-3] == 'MAS': #up-left
                        total +=1                         
            except IndexError:
                pass
            try:
                if valid_num(num) is True:
                    if input[num-1][i+1] + input[num-2][i+2] + input[num-3][i+3] == 'MAS': #up-right
                        total +=1        
            except IndexError:
                pass
            try:
                if valid_i(i) is True:
                    if input[num+1][i-1] + input[num+2][i-2] + input[num+3][i-3] == 'MAS': #down-left
                        total +=1       
            except IndexError:
                pass
            try:
                if input[num+1][i+1] + input[num+2][i+2] + input[num+3][i+3] == 'MAS': #down-right
                    total +=1   
            except IndexError:
                pass

print(total)