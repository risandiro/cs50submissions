import sys

def main():



def cma_check():
    if len(sys.argv) == 2:
        return True
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")


if __name__ == "__main__":
    main()
