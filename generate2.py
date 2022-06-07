"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 4"""

#only imports choice from random library
from random import choice


#no longer have to call random.choice because we are pulling choice from random when importing
coin = choice(["heads", "tails"])
print(coin)