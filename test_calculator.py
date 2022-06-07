"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 5"""

#specifically to test calculator.py functionality

from calculator import square

def main():
    test_square()


def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")

if __name__ == "__main__":
    main()

#if does nothing, all good!