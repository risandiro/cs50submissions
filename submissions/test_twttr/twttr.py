import sys

def main():
    word = input("Input: ")
    output = shorten(word)
    print("Output:", output)

def shorten(word):
    vowels = ["a", "e", "i", "o",  "u"]
    output = ""

    # for every character in the (length of) input
    for char in range(len(word)):
        # if the character (upper-or-lower case) is not in the "vowel" list
        if word[char].lower() not in vowels:
            # add it to the string
            output += word[char]
    return output

if __name__ == "__main__":
    main()
