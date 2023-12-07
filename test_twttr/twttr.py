def main():
    word = input("Input: ")
    answer = shorten(word)
    print(answer)


def shorten(word):
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    output = "Output: "

    counter = 0
    for letter in word:
        for i in range(len(vowels)):
            if letter == vowels[i]:
                counter += 1
        if counter == 0:
            output += letter
        counter = 0
    return output


if __name__ == "__main__":
    main()
