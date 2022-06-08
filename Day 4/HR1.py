# www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):
    leap = False
    if year >= 1900 or year <= 100000:
        if (year % 4) == 0:
            leap = True
            if (year % 100) == 0:
                leap = False
                if (year % 400) == 0:
                    leap = True
    return leap

year = int(input())
print(is_leap(year))