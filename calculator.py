"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 5"""

#define main function
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

#returns n * n, n being stand in number
def square(n):
    #when testing, change + and *
    return n * n

#want to make sure when I input my square function, want to make sure main
#is not automatically called in itself
if __name__ == "__main__":
    main()

# Need to test representative