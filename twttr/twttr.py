def main():
    input = input("Input: ")
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    counter = 0

def shorten(word):
    print("Output:", end=" ")
    for letter in word:
        for i in range(len(vowels)):
            if letter == vowels[i]:
                counter += 1
        if counter == 0:
            print(letter, end="")
        counter = 0
    print()






