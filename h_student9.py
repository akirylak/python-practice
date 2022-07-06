"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 8"""

#common to capitalize a class data type
#bare minimum to create a class
class Student:
    ...


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    #call the class variable
    student = Student()
    #classes have attributes
    student.name = input("Name: ")
    student.house = input("House: ")
    return student


if __name__ == "__main__":
    main()

'''
Class - blueprint for pieces of data, types of data
Allow you to invent your own data type and give it your own name
Create your own objects

Objects - when you use a class
'''
