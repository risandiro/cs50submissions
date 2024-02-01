import sys
from datetime import date

def main():
    get_date()


def get_date():
    today = str(date.today())
    y, m, d = today.split("-")
    y, m, d = int(y), int(m), int(d)

    try:
        prompt = input("Date of Birth: ")
        year, month, day = prompt.split("-")
        if len(year) == 4 and len(month) == 2 and len(day) == 2:
            year, month, day = int(year), int(month), int(day)


    except ValueError:
        sys.exit("Invalid date")







if __name__ == "__main__":
    main()
