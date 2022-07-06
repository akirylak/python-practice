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
    #can validate in a class, like if name exists or house is correct
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house




def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: " )
    house = input("House: ")
    return Student(name, house)



if __name__ == "__main__":
    main()

'''
Class - blueprint for pieces of data, types of data
Allow you to invent your own data type and give it your own name
Create your own objects

Objects - when you use a class
'''

