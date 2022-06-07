"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 6"""
#import CSV module
import csv

#sorted list
name = input("What's your name? ")
home = input("Where's your home? ")

#open in append mode!, do not overwrite to avoid errors
#dictionary writer to write
with open("students4.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    #write a dictionary with the following
    writer.writerow({"name": name, "home": home})