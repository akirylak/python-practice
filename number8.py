"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 3"""
#define main
def main():
    #call the function into x
    x = get_int()
    print(f"x is {x}")

#define function
def get_int():
    while True:
        #get input from user
        try:
            x = int(input("What's x? "))
        #return error if ValueError
        except ValueError:
            print("x is not an integer")
        else:
            #can just return x instead of break out of loop to return x
            return x

main()