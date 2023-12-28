
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():
    return {"name": input("Name: "), "house": input("House: ")}

# ---------------------------------------------
'''
def main():
    student = get student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    # return (name, house) -> a tuple
    return [name, house] # returns a list
'''

main()
