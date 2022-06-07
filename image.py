"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 6"""

#image files
import sys
#Pillow Library: PIL
from PIL import Image

#to store a list of images
images = []

#for argument in sys.argv
for arg in sys.argv[1:]:
    #documentation in PIL
    image = Image.open(arg)
    images.append(image)

#save to disk, open, close and save is handled in library
images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)