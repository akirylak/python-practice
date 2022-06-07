"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 4"""
#command line arguements
import sys

#check for errors
if len(sys.argv) < 2:
    sys.exit("Too Few Arguements")

#for loop to iterate over a list
#use slices to avoid printing argv[0]
for arg in sys.argv[1:]:
    print("Hello, my name is", arg)
