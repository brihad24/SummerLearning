no_stud = input()
stud_marks = dict()
output = ''

for i in no_stud:
    name = input()
    marks = float(input())
    stud_marks[marks] = [name]

stud_marks.sort()

print(stud_marks.name[1])

