import sys, re
from datetime import date

def main():
    current = date.today()
    user_input = input("Date of Brith: ")
    user_input = validate(user_input)
    print(user_input)


def validate(inp):
    current = str(date.today())
    print(current)
    yyyy = current.split("-", maxsplit=1)
    print(yyyy)
    yyyy = int(yyyy)

    try:
        if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", inp):
            year, month, day = inp.split("-")
            year, month, day = int(year), int(month), int(day)
            if year <= yyyy:
                user_input = date(year, month, day)
                return user_input

            else:
                raise ValueError
        else:
            raise ValueError

    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
