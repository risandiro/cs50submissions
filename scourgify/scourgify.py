import sys

def main():
    cma_check()
    try:

    except FileNotFoundError:
        sys.exit("could not re)


def cma_check():
    if sys.argv == 3:
        return
    elif sys.argv < 3:
        sys.exit("Too few command-line arguments")
    elif sys.argv > 3:
        sys.exit("Too many command-line arguments")


if __name__ == __"main"__:
    main()
