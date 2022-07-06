"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 7"""
import re

#prompt user for email
email = input("What's your email? ").strip()

#re.search(pattern, string, flags=0)
#there is an official standard for an email address
#specify a range of lowercase letters, do "a" hythen "z", no spaces no commas no separators
#to include range of uppercase letters, do "A" hyphen "Z", no spaces no commas no separators
#to include range of nubmers, do "0" hythen "9", no spaces no commas no separators
#to include an underscore "_", just include "_"
#[a-zA-Z0-9_] includes these characters
if re.search("^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
