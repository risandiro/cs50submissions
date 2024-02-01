import sys
from datetime import date

def main():
    get_date()


def get_date():
    today = date.today()
    y, m, d = today.split("-")
    y, m, d = int(x), int(y), int(z)

    try:
        prompt = input("Date of Birth: ")
        year, month, day = prompt.split("-")
        year, month, day = int(year), int(month), int(day)
        if 


    except ValueError:
        sys.exit("Invalid date")







if __name__ == "__main__":
    main()
