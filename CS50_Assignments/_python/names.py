# ---------------------------------------- sort a list

names = []
for _ in range(3):
    names.append(input("What's your name? "))
print(sorted(names))

# ---------------------------------------- basic functions of i/o

name = input("What's your name? ")

# if the file doesn't exist, python creates it
# "w" -> write (opens as a new tab and rewrites any content possibly there)
# "a" -> append (adds to a file)
# "r" -> read (read all lines and return them as a list)

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()

# -----

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

# ---------------------------------------- print all lines from a text file


with open("names.txt", "r") as file:
    # lines = file.readlines()
    # for line in lines
    #  -> we don't need to read them because for loop reads them also
    for line in file:
        print(line.rstrip())

# ---------------------------------------- copy the content from a text file to a local list

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

# ---------------------------------------- copy the content of csv file as a list of values

with open("students.csv") as file:
    for line in file:
        row = line.rstip().split(",")
        print(f"{row[0]} is in {row[1]}")

# ---------------------------------------- list of students where every student is a dict

students = []

with open("names.csv") as file:
    for line in file:
        name, house, home = line.rstrip().split(",")
        #student = {}
        #student["name"] = name
        #student["house"] = house
        student = {"name": name, "house": house, "home": home}
        students.append(student)

# ---------------------------------------- sort the data by a chosen key

def get_name(student):
    return student["name"]
# lambda student: student["name"])

def get_house(student):
    return student["house"]
# lambda student: student["house"])


for student in sorted(students, key=get_name, reverse=True):
    print(f"{student['name']} is in {student['house']} and lives {student['home']}")

for student in sorted(students, key=get_house):
    print(f"{student['name']} is in {student['house']} and lives {student['home']}")

# lambda indicates to python that this is an annonymous function that you just pass to another function
# we replace name with lambda, argument: return value
for student in sorted(students, key=lambda student: student["name"])
    print(f"{student['name']} is in {student['house']}")

# ------------------------------------------

# if you have commas in "names.csv" and want to use them without separating the values
# with csv you can use quotes to distinguish which commas are separators and which aren't
import csv

students = []
with open("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "house": row[1], "home": row[2]})
        # students.append(row)

    # for name, house, home in reader:
        # students.append({"name": name, "house": house, "home": home})


students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "house": row["house"], "home": row["home"]})
        # students.append(row)


    for student in sorted(students, key=lambda student: student["name"])
        print(student["house"])

# -------------------------------------------- writing data to csv

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

# ------------------------------------------- write data to csv as a list

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name,home])

# ------------------------------------------- write data to csv as a dictionary

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
