"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 7"""

#prompt user for email
email = input("What's your email? ").strip()

#split string at the @ symbol into 2 parts
username, domain = email.split("@")

#checking if there is a username present and the "." in domain is present
#2 boolean expressions
if username and "." in domain:
    print("Valid")
else:
    print("Invalid")