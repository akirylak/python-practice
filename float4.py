"""Code Created by Amber Linnea Kirylak for Harvard CS50P class lecture 0"""
#calculator with floats instead
x= float(input("What's x? "))
y = float(input("What's y? "))

#what if we want to round to the nearest integer?

#divided by
#round to the nearest by 2 digits
z = round(x / y, 2)

print(z)

"""option 2 by format string

print(f"{z:.2f}")

"""