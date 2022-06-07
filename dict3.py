"""Code Created by Amber Linnea Kirylak for Harvard CS50P class lecture 2"""

#dictionary with key:value pairs
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

#printing using for loop
for student in students:
    #print(students) --- will only print out keys
    #first must be student as it will print the first key
    #students[student] will print out the value
    print(student, students[student], sep=", ")