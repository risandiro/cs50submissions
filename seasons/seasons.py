import sys, re
from datetime import date

def main():
    get_date()


def get_date():
    today = str(date.today())
    y, m, d = today.split("-")
    y, m, d = int(y), int(m), int(d)

    try:
        prompt = input("Date of Birth: ")
        if matches := re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", prompt):


    except ValueError:
        sys.exit("Invalid date")







if __name__ == "__main__":
    main()
