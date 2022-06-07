"""Code Created by Amber Linnea Kirylak for Harvard CS50P class lecture 2"""

#list of 3 strings called students
students = ["Hermione", "Harry", "Ron"]

#range would find the number of the length of the list in students
for i in range(len(students)):
    #do not print(i), it will only print numbers
    #print(students[i]) will replace 0 with the range of the list in students
    print (students[i])

"""
if we print(i + 1, students[i])
we can print out the placement number and student name.

without +1, it will start at 0 not 1
"""