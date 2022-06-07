"""Code Created by Amber Linnea Kirylak for Harvard CS50P class lecture 2"""

def main():
    print_square(3)

#loop to print rows of print_row
def print_square(size):
    for i in range(size):
        print_row(size)

#how to print a row
def print_row(width):
    print("#" * width)

main()