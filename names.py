'''
names = []

for _ in range(3):
    names.append(input("What's your name? "))

print(sorted(names))
'''

name = input("What's your name? ")

# if the file doesn't exist, python creates it
# next we specify what we want to do with it "w", means write and allows to change the content
file = open("names.txt", "w")
file.write(name)
file.close()

