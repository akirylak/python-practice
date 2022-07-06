"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 7"""

#prompt users for Twitter URL
#extract username from Twitter URL


url = input("URL: ").strip()

#url is a string, replace is a method
username = url.replace("https://www.twitter.com/", "")

print(f"Username: {username}")

#not quite perfect as it does not account for http://, or twitter.com etc