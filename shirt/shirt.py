import sys

def main():


def input_check():
    if len(sys.argv) == 3:
        if sys.argv[1].endswith(".jpg") and sys.argv[2]


    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")




if __name__ == "__main__":
    main()
