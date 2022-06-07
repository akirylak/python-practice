"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 6"""
#import CSV module
import csv

#sorted list
students = []

with open('students2.csv') as file:
    #CSV documentation to read the file
    reader = csv.reader(file)
    for row in reader:
        #starts at 0 index
        students.append({"name": row[0], "home": row[1]})

'''
can also write
for name, home in reader:
    students.append({"name": name, "home": home})
'''

#look up lambda, a function without a name
for student in sorted(students, key=lambda student: student["name"]):
    #need to use single quotes to access keys, because you have double quotes for fstring
    print(f"{student['name']} is in {student['home']}")
