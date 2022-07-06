"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 8"""

#Dictionary of Keys and Values  Key:Value

def main():
    student = get_student()
    #cannot use double quotes in double quotes, need to use single quotes around keys
    #case-sensitive!!
    print(f"{student['name']} from {student['house']}")


def get_student():
    #empty dictionary
    student = {}
    #name of first key
    student["name"] = input("Name: ")
    #name of second key
    student["house"] = input("House: ")
    return student



if __name__ == "__main__":
    main()

