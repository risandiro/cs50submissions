import random


def main():
    print(generate_integer(1))

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
        return randrange(10)
    if level == 2:
        return randrange(100)
    if level == 3:
        return randrange(1000)


if __name__ == "__main__":
    main()
