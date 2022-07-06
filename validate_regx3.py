"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 7"""
import re

#prompt user for email
email = input("What's your email? ").strip()

#re.search(pattern, string, flags=0)

#wants to end the code in .edu, cannot use a literal "."
#need to use the escape character "\" backslash
if re.search(".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")