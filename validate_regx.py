"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 7"""
import re

#prompt user for email
email = input("What's your email? ").strip()

#re.search(pattern, string, flags=0)
if re.search("@", email):
    print("Valid")
else:
    print("Invalid")

#not perfect, same as validate.py but with regex