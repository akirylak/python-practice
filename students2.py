"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 6"""

with open('students.csv') as file:
    for line in file:
        #each line is a row, separated by commas is col
        #if you know that it returns 2 items in a list, you can assign  variable
        name, house = line.rstrip().split(',')
        #index like a list
        print(f"{name} is in {house}")