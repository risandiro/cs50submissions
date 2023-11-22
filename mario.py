def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print("#" * size, end="\n")
        i += 1

main()
