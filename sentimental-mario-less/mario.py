import sys

def main():
    while True:
        height = int(input("Height: "))
        if 0 < height <= 8:



    counter = height
    hash = 1

    while counter > 0:
        print(" " * (height - hash), end="")
        print("#" * hash)
        hash += 1
        counter -= 1

main()
