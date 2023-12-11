
names = []
for _ in range(3):
    names.append(input("What's your name? "))
print(sorted(names))

# ----------------------------------------

name = input("What's your name? ")

# if the file doesn't exist, python creates it
# "w" -> write (opens as a new tab and rewrites any content possibly there)
# "a" -> append (adds to a file)
# "r" -> read (read all lines and return them as a list)

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()

# ----------------------------------------

name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

with open("names.txt", "r") as file:
    # lines = file.readlines()
    # for line in lines
    #  -> we don't need to read them because for loop reads them also
    for line in file:
        print(line.rstrip())

# ----------------------------------------

# "r" -> read is the default, you don't have to specify
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")

# to make it more compact, but you can't actually work with the data itself this way

with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())

# ----------------------------------------

with open("students.csv") as file:
    for line in file:
        row = line.rstip().split(",")
        print(f"{row[0]} is in {row[1]}")

# ----------------------------------------

students = []

with open("names.csv") as file:
    for line in file:
        name, house, home = line.rstrip().split(",")
        #student = {}
        #student["name"] = name
        #student["house"] = house
        student = {"name": name, "house": house, "home": home}
        students.append(student)

def get_name(student):
    return student["name"]
# lambda student: student["name"])

def get_house(student):
    return student["house"]

for student in sorted(students, key=get_name, reverse=True):
    print(f"{student['name']} is in {student['house']} and lives {student['home']}")

for student in sorted(students, key=get_house):
    print(f"{student['name']} is in {student['house']} and lives {student['home']}")

# lambda indicates to python that this is an annonymous function that you just pass to another function
# we replace name with lambda, argument: return value
for student in sorted(students, key=lambda student: student["name"])
    print(f"{student['name']} is in {student['house']}")

# ------------------------------------------

import csv

students = []
with open("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "house": row[1], "home": row[2]})

    # for name, house, home in reader:
        # students.append({"name": name, "house": house, "home": home})
