"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 7"""
import re

#prompt user for email
email = input("What's your email? ").strip()

#re.search(pattern, string, flags=0)

#how to validate input so there is just an email but not a sentence.
#sample input:  My email address is malan@harvard.edu
if re.search("^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

'''
^  matches the start of the string
$  matches the end of the string or just before the new line at the end of the string
'''