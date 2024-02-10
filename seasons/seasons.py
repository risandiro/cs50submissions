import sys
from datetime import date

def main():
    current = date.today()
    user_input = input("Date of Brith: ")
    user_input = validate(user_input)
    print(user_input)


def validate(inp):
    try:
        year, month, day = inp.split("-")
        year, month, day = int(year), int(month), int(day)
        user_input = date(year, month, day)
        return user_input

    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
