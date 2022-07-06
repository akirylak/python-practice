"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 7"""

#prompt user for email
email = input("What's your email? ").strip()

#find the @ sign and the "."
#looking for 2 parameters
if "@" in email and "." in email:
    print('Valid')
else:
    print('Invalid')

#universally searches for @ sign and a period ".", however it does not confirm if the input is actually an email
#email needs a .com/.net.gov at the end