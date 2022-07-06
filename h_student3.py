"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 8"""


def main():
    name, house = get_student()
    print(f"{name} from {house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    #return multiple values as a tuple.  Tuple is 1 value with 2 things
    return (name, house)



if __name__ == "__main__":
    main()

'''
tuple - return multiple values separated by comma
'''