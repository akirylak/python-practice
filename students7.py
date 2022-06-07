"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 6"""

#sorted list
#how to sort by first name not by sentence
students = []

with open('students.csv') as file:
    for line in file:
        name, house = line.rstrip().split(",")
        #another way to create key values in a dictionary
        student = {"name": name, "house": house}
        students.append(student)

#look up lambda, a function without a name
for student in sorted(students, key=lambda student: student["name"]):
    #need to use single quotes to access keys, because you have double quotes for fstring
    print(f"{student['name']} is in {student['house']}")

#lambda can take multiple parameters
#can have more than one lambda function