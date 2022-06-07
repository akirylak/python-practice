"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 3"""
#define main
def main():
    #call the function into x
    x = get_int("What's x? ")
    print(f"x is {x}")

#define function
def get_int(prompt):
    while True:
        #we can return the get user input
        try:
            return int(input(prompt))
        #return error if ValueError
        except ValueError:
            #we can pass instead of printing over and over again
            pass

''' adding prompt will universally will allow you to reuse code to ask not just "what's x" but also "what's y"
'''
main()