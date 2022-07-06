"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 7"""

#prompt users for Twitter URL
#extract username from Twitter URL

url = input("URL: ").strip()

#url is a string, removeprefix removes information in the beginning of a string
username = url.removeprefix("https://www.twitter.com/")

print(f"Username: {username}")

