"""Code Created by Amber Linnea Kirylak for Harvard CS50P class lecture 0"""
#calculator with floats instead
x= float(input("What's x? "))
y = float(input("What's y? "))

#what if we want to round to the nearest integer?

z = round(x + y)

#printing with format to add commas, using f string
#colon comma :, formats the number to add commas
print(f"{z:,}")
