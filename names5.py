"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 6"""

name = input("What's your name? ")

#with - open and close automatically
#open first, call file and type, assign variable with as
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
