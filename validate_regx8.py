"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 7"""
import re

#prompt user for email
email = input("What's your email? ").strip()

#re.search(pattern, string, flags=0)

# \w is a word character alphanumeric character plus underscore, replaces [a-zA-Z0-9_]
if re.search("^\w+@\w+\.(edu|com|gov|net|org)$", email):
    #^ start matching at beginning of the string
    print("Valid")
else:
    print("Invalid")

'''
patterns you can use in expressions
\d  decimal digit
\D  not a decimal digit
\s  whitespace chracters
\S  not a whitespace characters
\w  word character as well as numbers and the underscore only
\W  not a word character
|  vertical bar means OR
()  a group
(?:   )  non-capturing version
" "  can use a literal space (without quotes)
'''