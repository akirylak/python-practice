"""Code Created by Amber Linnea Kirylak for Harvard CS50P class lecture 0"""

#define convention
def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to)

"""if you just run def without calling the function, nothing will happen"""

main()
