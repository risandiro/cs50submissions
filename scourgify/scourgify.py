import sys, csv

def main():
    cma_check()
    data = []
    try:

        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                first_name, last_name = row["name"].strip().split(",")
                data


    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


def cma_check():
    if sys.argv == 3:
        return
    elif sys.argv < 3:
        sys.exit("Too few command-line arguments")
    elif sys.argv > 3:
        sys.exit("Too many command-line arguments")


if __name__ == __"main"__:
    main()
