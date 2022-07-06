"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 8"""

#common to capitalize a class data type
#bare minimum to create a class
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
    #only takes 1 arguement
    def __str__(self):
        #return f string
        return f"{self.name} from {self.house}"



def main():
    student = get_student()
    #if you just print(student), you get the representation in memory
    #used __str__ to call itself in class
    print(student)

def get_student():
    name = input("Name: " )
    house = input("House: ")
    return Student(name, house)



if __name__ == "__main__":
    main()

'''
__str__  - method, define in class, python will automatically call the function for you
there are many methods that are part of class that starts with __.

'''