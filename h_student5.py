"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 8"""


def main():
    student = get_student()
    #override the user's input if student is Padma
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
        #TypeError: 'tuple' object does not support item assignment (immutibility error, design of a tuple)
        #needed to change line 18 to a list not a tuple
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    #[] are a list, () is a tuple
    return [name, house]



if __name__ == "__main__":
    main()

