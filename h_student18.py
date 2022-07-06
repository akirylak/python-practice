"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 8"""

#variables and function cannot be the same
class Student:
    def __init__(self, name, house):
        #no longer need error check here
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name

    #getter - function that gets some attribute
    @property
    def house(self):
        return self._house

    #setter - function that sets some value
    @house.setter
    def house(self, house):
        #error check to prevent hijacking
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house


def main():
    student = get_student()
    #below raises value error
    #student.house = "Number Four, Privet Drive"
    print(student)

def get_student():
    name = input("Name: " )
    house = input("House: ")
    return Student(name, house)



if __name__ == "__main__":
    main()

'''
properties - attribute that has more defense mechanisms in place
@property
decorators - functions that modify the behavior of other functions
'''