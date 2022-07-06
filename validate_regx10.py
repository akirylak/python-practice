"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 7"""
import re

#prompt user for email
#can format input to all lowercase on input, however
email = input("What's your email? ").strip()#.lower()

#re.search(pattern, string, flags=0)

# \w is a word character alphanumeric character plus underscore, replaces [a-zA-Z0-9_]
#can format email when checking as email.lower()
#OR we USE FLAGS!
'''
re.IGNORECASE   ignore case of user input
re.MULTILINE   Mutiple lines
re.DOTALL   anycharacter plus new lines
'''

if re.search("^\w+@(\w+\.)?\w+\.edu)$", email, re.IGNORECASE):
    #group around parenthesis (\w+\.)?  can be in 1 or 0 times
    print("Valid")
else:
    print("Invalid")

'''
why is malan@cs50.harvard.edu invalid?
Because only word characters are accepted
To retool, you can group ideas together.

A|B  either A or B
(...)  a group
(?..)  a non-capuring version
'''