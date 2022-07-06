"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 7"""

#prompt users for Twitter URL
#extract username from Twitter URL
import re

#re.sub(pattern, replace, string, count=0, flags = 0)
#re.sub is substitution

url = input("URL: ").strip()

if matches := re.search("^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))
