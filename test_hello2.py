"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 5"""

from hello import hello

def test_default():
    assert hello("David") == "hello, David"

def test_arguement():
    assert hello() == "hello, world"
