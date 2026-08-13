# This program takes marks of 5 students as input and stores them in an array (list) and then prints them.
marks = []
size = 5

for i in range(size):
    num = int(input("Enter mark for student: "))
    marks.append(num)

for i in range(size):
    print(marks[i])
    