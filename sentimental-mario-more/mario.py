def main():
    while True:
        try:
            height = int(input("Height: "))
            if 0 < height <= 8:
                break
            raise
        except:
            print("Enter a number between 1 and 8 inclusive")

    counter = height
    hash = 1

    while counter > 0:
        print(" " * (height - hash), end="")
        print("#" * hash, end="  ")
        print("#" * hash)
        hash += 1
        counter -= 1


main()
