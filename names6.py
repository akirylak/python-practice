"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 6"""

#reading a file
with open("names.txt", "r") as file:
    lines = file.readlines()
#iterate over the file
for line in lines:
    #need to add end="" or line.rstrip() so not to double space
    print("hello,", line.rstrip())

