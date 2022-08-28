# Question = https://www.hackerrank.com/challenges/counting-valleys/problem

steps = int(input())
path = input()
mountain = 0
valley = 0

for s in path:
    
    if s == 'U':
        mountain += 1
        
        if mountain == 0:
            valley += 1
            
    else:
        mountain -= 1
        
print(valley)