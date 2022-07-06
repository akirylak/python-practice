"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Lecture 8"""

#Dictionary of Keys and Values  Key:Value

def main():
    student = get_student()
    #dictionaries are mutable
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")

#consolidate code to return a dictionary instead of creating dictionary first
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}



if __name__ == "__main__":
    main()

