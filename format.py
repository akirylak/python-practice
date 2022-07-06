"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 7"""

'''
re.match(patten, string, flags=0)  matches the start of the string
re.fullmatch(pattern, string,flag=0)  matches the start and end of the string
'''

import re

name = input("What's your name? ").strip()
print(f"hello, {name}")