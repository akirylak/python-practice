"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 4"""

#requests allow the python to make requests through API
#pip install requests

#JSON, javascript object notation, langauge agnostic format to read or write json
import sys
import requests

#if the length of the command line arguement is not equal to 2 arguements, exit
if len(sys.argv) != 2:
    sys.exit()

#variable response, use requests to get the API request and concatinate with arguement 1.  Arguements start with index of 0
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())

#returns a json response of a dictionary
#python comes with a library called json

