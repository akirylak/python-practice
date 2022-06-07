"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 3"""
#define main
def main():
    #call the function into x
    x = get_int()
    print(f"x is {x}")

#define function
def get_int():
    while True:
        #we can return the get user input
        try:
            return int(input("What's x? "))
        #return error if ValueError
        except ValueError:
            #we can pass instead of printing over and over again
            pass

main()