def main():
    text = input("Text: ")

    letters = count_letters(text)
    words = count_words(text)
    sentances = count_sentances(text)

    L = letters / words * 100.00
    S = sentances / words * 100.00
    index = 0.0588 * L - 0.296 * S - 15.8

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
    counter = 1
    next = False

    text.strip()
    for character in text:
        if character == ' ' and next == True:
            counter += 1
            next = False

        elif character == '.' or character == '?' or character == '!':
            next = True
            continue

    return counter


main()
