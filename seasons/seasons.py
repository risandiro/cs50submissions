import sys
from datetime import date

def main():
    get_input()


def get_input():
    try:
        date = input("Date of Birth: ")
        year, month, day = date.split("-")


    except ValueError:
        sys.exit("Invalid date")





if __name__ == "__main__":
    main()
