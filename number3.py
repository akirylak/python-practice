"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 3"""
#prompt user for integer
#try / except

try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")

'''
if type in integers will pass.
if type in cat, returns NameError: name "x" is not defined.
it is caused by the order of operations in x = int(input("What's x? "))

go to number4.py to see solution
'''