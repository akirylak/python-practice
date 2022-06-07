"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 5"""

def main():
    name = input("What's your name? ")
    #print function
    print(hello(name))

def hello(to="world"):
    #print("hello,", to) will not test as it is not returning a value
    return f"hello, {to}"


if __name__ == "__main__":
    main()