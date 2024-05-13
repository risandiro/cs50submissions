def main():
    height = int(input("Height: "))
    for i in range(height):
        print_row(height)
        height -= height

def print_row(height: int):
        print("#" * height)

main()
