'''
names = []

for _ in range(3):
    names.append(input("What's your name? "))

print(sorted(names))
'''

name = input("What's your name? ")

# if the file doesn't exist, python creates it
# "w" -> write (opens as a new tab and rewrites any content possibly there)
# "a" -> append

file = open("names.txt", "a")
file.write(name)
file.close()

