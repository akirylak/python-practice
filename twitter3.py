"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 7"""

#prompt users for Twitter URL
#extract username from Twitter URL
import re

#re.sub(pattern, replace, string, count=0, flags = 0)
#re.sub is substitution

url = input("URL: ").strip()

username = re.sub("https://twitter.com/", "", url)

print(f"Username: {username}")

