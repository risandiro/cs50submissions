
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

names = []

# "r" -> read is the default, you don't have to specify
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
