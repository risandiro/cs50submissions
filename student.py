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
# besides attributes and instance variables it can contain methods(functions)
# with a class you get also a function, whose name is identical to the class name
class Student:
    # instance method called Dunder innit method
    # if we call Student as a function, this function is going to be called
    # self gives to access to the currect object that has been created (name can be different)
    def __init__(self, name, house):
        # what we are doing is adding instance variables to objects
        self.name = name
        self.house = house

def main3():
    student = get_student3()
    # name and house are variables inside of an object whose type is Student
    # more precisely name and house are instance variables
    print(f"{student.name} from {student.houske}")


def get_student3():
    # classes creates objects(instances), you create objects from classes
    student = Student()
    # store attributes inside of the class
    ''' student.name = input("Name: ")
    student.house = input("House: ") '''
    name = input("Name: ")
    house = input("House: ")
    # we are treating Student as a function, passing in two values
    # construct call, a call that is going to construct(instantiate) a student object for me
    student = Student(name, house)
    return student



main3()
