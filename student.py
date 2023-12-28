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

# class defines a custom new data type, contains attributes
# with a class you get also a function, whose name is identical to the class name
class Student:
    ...

def main3():
    student = get_student3()
    # access attributes from the class
    # name and house are variables inside of an object whose type is Student
    # more precisely name and house are attributes/instance variables
    print(f"{student.name} from {student.house}")


def get_student3():
    # classes creates objects(instances), you create objects from classes
    student = Student()
    # store attributes inside of the class
    ''' student.name = input("Name: ")
    student.house = input("House: ") '''
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student



main3()
