"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 7"""

'''
re.match(patten, string, flags=0)  matches the start of the string
re.fullmatch(pattern, string,flag=0)  matches the start and end of the string
'''

import re

name = input("What's your name? ").strip()
#what if the user inputs last name, first name
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"hello, {name}")