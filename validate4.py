"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 7"""

#prompt user for email
email = input("What's your email? ").strip()

#split string at the @ symbol into 2 parts
username, domain = email.split("@")

#checking if there is a username present and the domain name ends with .edu
#2 boolean expressions
if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")

#problem with code, only searches for .edu, not .com, .net etc