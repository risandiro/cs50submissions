'''
names = []

for _ in range(3):
    names.append(input("What's your name? "))

print(sorted(names))
'''

name = input("What's your name? ")

open("names.txt", "w")

