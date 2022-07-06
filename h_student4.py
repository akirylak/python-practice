"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 8"""


def main():
    student = get_student()
    #tuple is immutable where we can index it
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    #return multiple values as a tuple.  Tuple is 1 value with 2 things
    return (name, house)



if __name__ == "__main__":
    main()

'''
tuple - return multiple values separated by comma
tupples cannot be changed.  Lists can be changed.
'''