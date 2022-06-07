"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 6"""

#sorted list
students = []

with open('students.csv') as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)