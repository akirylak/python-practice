"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 3"""
#prompt user for integer
#try / except

try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")

#indentation is important
'''
input: 50, output: prints x is 50
input: cat. output: prints cat is not an integer
'''