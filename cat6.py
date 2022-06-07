"""Code Created by Amber Linnea Kirylak for Harvard CS50P class lecture 2"""

#ask a true or false question using while
i = 0
#while i is less than or equal to 3
while i < 3:
    print("meow")
    #incriment i with fewer keystrokes, python does not have ++ or -- like in C
    i = i+= 1

"""
if we were to have i = 0 and initiate the code, it would print 'meow' 4 times because it counts 0 as the first operation
to fix this we change while i <= 3 to while i < 3:
we go up to 3 not through 3
"""