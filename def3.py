"""Code Created by Amber Linnea Kirylak for Harvard CS50P class lecture 0"""

#define the new function called hello,
#all code a part of def hello() must be indented
#to is the arguement, think of it as saying hello to what?
#to="world" is a default value if user does not give user input
def hello(to="world"):
    print("hello,", to)

#this function will output hello, world
hello()
#get user input
name = input("What's your name? ")
#output hello, user input
hello(name)