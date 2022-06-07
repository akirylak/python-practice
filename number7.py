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
        #break out of loop if try is True
        else:
            break
    #return value
    #if the function is to hand over a value
    return x

main()