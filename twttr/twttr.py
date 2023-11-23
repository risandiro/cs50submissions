input = input("Input: ")
vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
output = ""

for c in input:
    if c != vowels[0]:
        output += c

print("Output:", output)
