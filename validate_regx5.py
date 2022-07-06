"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 7"""
import re

#prompt user for email
email = input("What's your email? ").strip()

#re.search(pattern, string, flags=0)

#need to solve the issue of malan@@@@@harvard.edu
#[^@] means anything except the @ sign
if re.search("^[^@]+@[^@]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

'''
[]  set of characters, specify a set of characters
[^]  complementing the set, excluding a set of characters ^
'''
