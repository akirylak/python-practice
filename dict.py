"""Code Created by Amber Linnea Kirylak for Harvard CS50P class lecture 2"""

#dictionaries are keys and values
#list is a set of multiple values

students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

#to print both lists
for i in range(len(students)) and range(len(houses)):
    print(students[i], houses[i])

#this is faulty as it is hard coded.