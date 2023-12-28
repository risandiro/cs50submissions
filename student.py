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

# class creates a custom data type, contains attributes
# classes creates objects/instances
class Student:
    ...

def main3():
    student = get_student3()
    print(f"{student.name} from {student.house}")


def get_student3():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student


main3()
