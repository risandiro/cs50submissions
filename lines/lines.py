import sys

def main():
    cma_check()
    file_check()
    counter = 0
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                line = line.strip()
                print(line)
                if line.startswith("#") or line.startswith("'''") or line.startswith('"""'):
                    continue
                elif len(line) == 0:
                    continue
                counter += 1
        print(counter)
    except FileNotFoundError:
        sys.exit("File does not exist")


def cma_check():
    if len(sys.argv) == 2:
        return
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

def file_check():
    if sys.argv[1].endswith(".py"):
        return
    else:
        sys.exit("Not a Python file")


if __name__ == "__main__":
    main()
