import random


def main():
    i, correct = int(0), int(0)
    level = get_level()
    while i != 10:
        x, y = generate_integer(level), generate_integer(level)

        mistake = int(0)
        while mistake < 3:
            print (f"{x} + {y} =", end=" ")
            try:
                answer = int(input())
                if answer != (x + y):
                    print("EEE")
                    mistake += 1
                else:
                    i += 1
                    break
            except ValueError:
                print("EEE")
                mistake += 1

        if mistake == 3:
            print (f"{x} + {y} = {x + y}")
            i += 1
            correct =+ 1

    print(f"Score: {10 - correct}")

# -----------------------------------------------------------------------

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                return level

        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randrange(10)
    if level == 2:
        return random.randrange(100)
    if level == 3:
        return random.randrange(1000)


if __name__ == "__main__":
    main()
