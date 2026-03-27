def main():
    word = input("Input: ")
    shorten(word)


def shorten(word):
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    print("Output:", end=" ")

    counter = 0
    for letter in word:
        for i in range(len(vowels)):
            if letter == vowels[i]:
                counter += 1
        if counter == 0:
            print(letter, end="")
        counter = 0
    print()


if __name__ == "__main__":
    main()
