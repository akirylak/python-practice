"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 6"""

#print a sorted list, need to read one list and write a sorted list in an empty list
names = []

#default is read
with open("names.txt") as file:
        for line in file:
            names.append(line.rstrip())

#descending order
for name in sorted(names, reverse=True):
    print(f"hello, {name}")