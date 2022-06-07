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

#sort by key "house"
def get_house(student):
    return student["house"]

for student in sorted(students, key=get_house):
    #need to use single quotes to access keys, because you have double quotes for fstring
    print(f"{student['name']} is in {student['house']}")