"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 6"""

#sorted list
#how to sort by first name not by sentence
students = []

with open('students.csv') as file:
    for line in file:
        name, house = line.rstrip().split(",")
        #create a dictionary
        student = {}
        #create key values
        student["name"] = name
        student["house"] = house
        students.append(student)

for student in students:
    #need to use single quotes to access keys, because you have double quotes for fstring
    print(f"{student['name']} is in {student['house']}")