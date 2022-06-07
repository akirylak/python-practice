"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 5"""

from calculator import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0

#run pytest test_pytest.py