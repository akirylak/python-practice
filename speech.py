"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 4"""

#pip is the python package command to install packages to the computer/cloud
'''
to install, in terminal.  pip install cowsay
'''

import cowsay
import sys

#print ascii cow
if len(sys.argv) == 2:
    #concatinate strings
    cowsay.cow("Hello, " + sys.argv[1])
else:
    pass

#print ascii trex
if len(sys.argv) == 2:
    #concatinate strings
    cowsay.trex("Hello, " + sys.argv[1])
else:
    pass

