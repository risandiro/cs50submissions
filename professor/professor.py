import random


def main():
    i = 0
    while i != 10:
        level = get_level()
        x, y = generate_integer(level), generate_integer(level)
        print (f"{x} + {y} =", end=" ")
        answer = int(input())

        mistake = 0
        try:
            if mistake < 4:
                if answer != (x + y):
                    print("EEE")
                    mistake += 1
                    raise ValueError
                else:
                    i += 1
            else:
                print (f"{x} + {y} ={x + y}")
                i += 1



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
