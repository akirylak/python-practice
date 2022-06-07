"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 6"""

#empty list called names
names = []

#loop 3 times
for _ in range(3):
    #input
    name = input("What's your name? ")
    #add to list
    names.append(name)


#sort list in a loop
for name in sorted(names):
    print(f"hello, {name}")

'''
can also code

for _ in range(3):
    names.append(input("What's your name? "))

'''