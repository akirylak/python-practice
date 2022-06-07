"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 3"""
#prompt user for integer
#try / except

try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

'''
code will try to get user input,
if integer, will execute else.  if string like "cat", it will
execute the except ValueError