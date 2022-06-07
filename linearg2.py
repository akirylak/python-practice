"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 4"""
#command line arguements
import sys

#sys.argv
#prints whatever is typed as the first arguement after calling the program
#lets try
try:
    print("Hello, my name is", sys.argv[1])

except IndexError:
    print("Too Few Arguements")