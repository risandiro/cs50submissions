import random


def main():
    level = get_level()
    x, y = generate_integer(level), generate_integer(level)
    


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
