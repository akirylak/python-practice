"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 5"""

from hello import hello

def test_default():
    assert hello("David") == "hello, David"

#for loop to test arguement
def test_arguement():
    for name in ["David", "Charles", "Ron"]:
        assert hello(name) == f"hello, {name}"
#takes longer to do it this way