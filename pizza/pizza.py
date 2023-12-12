import tabulate

def main():
    cma_check()
    file_check()



def cma_check():
    if len(sys.argv) == 2:
        return
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

def file_check():
    if sys.argv[1].endswith(".csv"):
        return
    else:
        sys.exit("Not a Python file")


if __name__ == "__main__":
    main()
