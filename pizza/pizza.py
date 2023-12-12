import csv, sys
from tabulate import tabulate

def main():
    cma_check()
    file_check()
    try:
        menu = []
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                menu.append({"Regular Pizza": row["Regular Pizza"], "Small": row["Small"], "Large": row["Large"]})
            print(tabulate(menu), headers="firstrow", tablefmt="grid")



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
    if sys.argv[1].endswith(".csv"):
        return
    else:
        sys.exit("Not a Python file")


if __name__ == "__main__":
    main()
