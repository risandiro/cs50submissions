class Student:
    ...
    


def main():
    student = get_student()
    if student["name"] == "Padma"
        student["house"] = "Gryffindor"
    print(f"{student['name']} from {student['house']}")

def get_student():
    return {"name": input("Name: "), "house": input("House: ")}

# ---------------------------------------------

def main2():
    student = get_student2()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student2():
    name = input("Name: ")
    house = input("House: ")
    # return (name, house) -> a tuple
    return [name, house] # returns a list

# ---------------------------------------------


main2()
