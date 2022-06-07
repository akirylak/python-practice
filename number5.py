"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 3"""
#prompt user for integer
#try / except

#use while loop to loo forever
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

print(f"x is {x}")
