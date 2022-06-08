# https://www.hackerrank.com/challenges/python-print/problem

num = int(input())
output = ''

for i in range(num+1):
    if i > 0:
        output += str(i)

print(output)