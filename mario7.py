"""Code Created by Amber Linnea Kirylak for Harvard CS50P class lecture 2"""

def main():
    print_square(3)

def print_square(size):
    #for each row in square
    for i in range(size):
        #for each brick in row
        for j in range(size):
            #print # but not a new line at the end
            print("#", end="")
        #prints a new line
        print()

main()