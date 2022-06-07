"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 4"""
#command line arguements
import sys

#sys.argv
#prints whatever is typed as the first arguement after calling the program

if len(sys.argv) < 2:
    print("Too Few Arguements")
elif len(sys.argv) > 2:
    print("Too Many Arguements")
else:
    print("Hello, my name is", sys.argv[1])

