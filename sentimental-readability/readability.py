def main():
    text = input("Text: ")
    print(count_letters(text))









# index = 0.0588 * L - 0.296 * S - 15.8

def count_letters(text):
    counter = 0

    for character in text:
        if character.isalpha():
            counter += 1

    return counter


def count_words(text):
    counter = 0
    next = False

    for character in text:
        if character == ' ' and next = True:
            counter += 1
            next = False

        else if character == ' ':
            next = True

# def count_sentances():


main()
