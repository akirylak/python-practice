"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 5"""

from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

#run pytest test_pytest.py