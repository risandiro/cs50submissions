import sys

def main():
    height = int(input("Height: "))
    if height < 0:
        sys.exit("Only positive integers")

    counter = height
    hash = 1

    while counter > 0:
        print(" " * (height - hash), end="")
        print("#" * hash)
        hash += 1
        counter -= 1

main()
