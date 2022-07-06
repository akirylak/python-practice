"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 7"""

'''
re.match(patten, string, flags=0)  matches the start of the string
re.fullmatch(pattern, string,flag=0)  matches the start and end of the string

(...)  Capturing
(?:...)  non-capturing version, don't bother capturing
'''

import re

name = input("What's your name? ").strip()
#look for pattern of Last comma First
#parenthesis to capture the .+
matches = re.search("^(.+), (.+)$", name)
#groups() are the groups on parenthesis above
if matches:
    last, first = matches.groups()
    name = f"{first} {last}"

print(f"hello, {name}")