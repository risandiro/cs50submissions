from random import randint

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

number = randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess != number:
                if guess > number:
                    print("Too large!")
                else:
                    print("Too small!")
            else:
                print("Just right!")
                break

    except ValueError:
        pass
