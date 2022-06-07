"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 4"""
#command line arguements
import sys

#check for errors
if len(sys.argv) < 2:
    sys.exit("Too Few Arguements")
elif len(sys.argv) > 2:
    sys.exit("Too Many Arguements")

#print nametag
print("Hello, my name is", sys.argv[1])

