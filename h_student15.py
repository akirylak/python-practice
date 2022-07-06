"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 8"""

#common to capitalize a class data type
#bare minimum to create a class
#add a 4th argument
class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.patronus = patronus

    #only takes 1 arguement
    def __str__(self):
        #return f string
        return f"{self.name} from {self.house}"
    #method of a class
    def charm(self):
        if self.patronus == "Stag":
            return "🐎"
        elif self.patronus == "Otter":
            return "🦦"
        elif self.patronus =="Jack Russell Terrier":
            return "🐕"
        else:
            return "🪄"


def main():
    student = get_student()
    #if you just print(student), you get the representation in memory
    #used __str__ to call itself in class
    print("Expecto Patronum!")
    print(student.charm())

def get_student():
    name = input("Name: " )
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)



if __name__ == "__main__":
    main()

'''
Classes can also have functions built in or "methods"
'''