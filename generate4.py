"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 4"""

import random

#shuffle cards
cards = ["jack", "queen", "king"]
#shuffle the list of cards
random.shuffle(cards)
for i in cards:
    print(i)

#or you can do for card in cards: print(cards)