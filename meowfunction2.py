"""Code Created by Amber Linnea Kirylak for Harvard CS50P class lecture 2"""

#define the main function to call meow 3 times
def main():
    #needs to set get_number() variable to another value
    number = get_number()
    #needs to call the variable number
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            #return the value to get_number()
            return n

"""
can use break but must return like this
def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            #return the value to get_number()
            break
    return n
"""

#define the meow function as the loop
def meow(n):
    for _ in range(n):
        print("meow")

#call main
main()