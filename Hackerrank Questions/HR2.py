# Question: https://www.hackerrank.com/challenges/drawing-book/problem

n = int(input())
p = int(input())

from_front = p//2
from_back = n//2 - p//2
print(min(from_front,from_back))