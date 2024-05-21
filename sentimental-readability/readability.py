def main():
    text = input("Text: ")
    print(count_letters(text))
    print(count_words(text))
    print(count_sentances(text))









# index = 0.0588 * L - 0.296 * S - 15.8

def count_letters(text: str):
    counter = 0

    for character in text:
        if character.isalpha():
            counter += 1

    return counter


def count_words(text: str):
    counter = 1
    next = False

    text.strip()
    for character in text:
        if character != ' ' and next == True:
            counter += 1
            next = False

        elif character == ' ':
            next = True
            continue

    return counter


def count_sentances(text: str):
    counter = 0
    next = False

    text.strip()
    for character in text:
        if character != '.' or character != '?' or character != '!' and next == True:
            counter += 1
            next = False

        elif character == '.' or character == '?' or character == '!':
            next = True
            continue

    return counter


main()
