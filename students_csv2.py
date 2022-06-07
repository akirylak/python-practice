"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 6"""
#import CSV module
import csv

#sorted list
students = []

with open('students3.csv') as file:
    #DictReader instead of reader
    #dictionary of columns
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})



#look up lambda, a function without a name
for student in sorted(students, key=lambda student: student["name"]):
    #need to use single quotes to access keys, because you have double quotes for fstring
    print(f"{student['name']} is in {student['home']}")
