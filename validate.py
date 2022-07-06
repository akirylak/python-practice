"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 7"""

#prompt user for email
email = input("What's your email? ").strip()

#find the @ sign
if "@" in email:
    print('Valid')
else:
    print('Invalid')

#universally searches for @ sign, however it does not confirm if the input is actually an email
#email needs a .com/.net.gov at the end