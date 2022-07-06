"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 7"""

'''
re.match(patten, string, flags=0)  matches the start of the string
re.fullmatch(pattern, string,flag=0)  matches the start and end of the string

(...)  Capturing
(?:...)  non-capturing version, don't bother capturing
'''

import re

name = input("What's your name? ").strip()

#must use a :=  the walrus operator
if matches := re.search("^(.+), (.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")