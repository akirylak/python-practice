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
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"

'''
or use
if matches:
    name = matches.group(2) + " " + matches.group(1)

the reason we start counting in 1, is because there is something else in 0 according to documentation
'''

print(f"hello, {name}")