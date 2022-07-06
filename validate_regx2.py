"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 7"""
import re

#prompt user for email
email = input("What's your email? ").strip()

#re.search(pattern, string, flags=0)

#.*@.* something or nothing to the left of @ and something or nothing to the right of @, but excepts nothing
#needs to be .+@.+ something to the left of @ and something to the right of @, but excepts nothing
# can use ..*@..* something to the left of @ and something to the right of @, but excepts nothing, same as .+
if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")

'''
pseudocode pattern needed
something to the left
@ sign
something to the right
ends with . and 3 character strings

REGEX Pattern def
.   any character except a new line
*   0 or more repetitions
+   1 or more repetitions
?   0 or 1 repetition
{m}   m repetitions, M representing a number of repetitions
{m,n}  m-n repetitions, m-n representing a range of repetitions

'''