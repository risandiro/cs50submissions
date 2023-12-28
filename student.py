def main():


def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student # returns a dictionary

# ---------------------------------------------
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
