"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 6"""

#reading a file
with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())

