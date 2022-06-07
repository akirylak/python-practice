"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 6"""

with open('students.csv') as file:
    for line in file:
        #each line is a row, separated by commas is col
        row = line.rstrip().split(',')
        #index like a list
        print(f"{row[0]} is in {row[1]}")