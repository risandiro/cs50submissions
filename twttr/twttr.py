s = input("Input: ")
vowels = "a", "A", "e", "E", "i", "I", "o", "O", "u", "U"

print("Output: ", end="")

for c in s:
    if c != vowels:
        print(c, end="")

print()
