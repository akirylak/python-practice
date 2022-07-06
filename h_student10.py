"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 8"""

#common to capitalize a class data type
#bare minimum to create a class
class Student:
    #methods, classes come with certain methods that can define
    #object oriented programming
    #impliment the initialization of an object in python
    #self calls the current object, convention is to call it "self"
    #gets access to the current object created
    #instancec variable __init__
    def __init__(self, name, house):
        #new attribute called name
        self.name = name
        #new attribute called house
        self.house = house




def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: " )
    house = input("House: ")
    #passing a function with name and house.
    #constructor call
    #users student class as the template
    student = Student(name, house)
    return student


if __name__ == "__main__":
    main()

'''
Class - blueprint for pieces of data, types of data
Allow you to invent your own data type and give it your own name
Create your own objects

Objects - when you use a class
'''
