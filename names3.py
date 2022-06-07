"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 6"""

#ask for user input
name = input("What's your name? ")

#save value to a file
#create a file, open it, call the name, can write, read or append
file = open("names.txt", "w")
file.write(name)
file.close()

#only can write 1 name as everytime you rerun the code
#you rewrite the file