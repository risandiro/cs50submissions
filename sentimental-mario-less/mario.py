def main():
    height = int(input("Height: "))
    blank = int(1)
    while height > 0:
        print(" " * (height - blank))
        print("#" * blank)
        blank += 1
        height -= 1

main()
