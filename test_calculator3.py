"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 4"""

#specifically to test calculator.py functionality

#use the assert function

from calculator import square

def main():
    test_square()

#use try and except to output user friendly code
def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")


if __name__ == "__main__":
    main()

#if does nothing, all good!