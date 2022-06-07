"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 5"""

#specifically to test calculator.py functionality

#use the assert function

from calculator import square

def main():
    test_square()


#will create non-userfriendly output
def test_square():
    assert square(2) == 4
    assert square(3) == 9

if __name__ == "__main__":
    main()

#if does nothing, all good!