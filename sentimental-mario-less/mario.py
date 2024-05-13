def main():
    height = int(input("Height: "))
    blank = int(0)
    while height > 0:
        print("#" * height)
        height -= 1

main()
