"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 7"""
import re

#prompt user for email
#can format input to all lowercase on input, however
email = input("What's your email? ").strip()#.lower()

#the regular expression browsers use today
if re.search("^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", email, re.IGNORECASE):
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