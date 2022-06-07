"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 6"""

#ask for user input
name = input("What's your name? ")

#save value to a file
#create a file, open it, call the name, can write, read or append
file = open("names.txt", "a")
#cannot use end="", need to manuall format new line
file.write(f"{name}\n")
file.close()

#need to append to write the names and when reruning the code, you
#add to the list