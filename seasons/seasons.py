import sys, re
from datetime import date

def main():
    validated = validate(get_date())
    yy, mm, dd = validated[0], validated[1], validated[2]
    


def get_date():
        prompt = input("Date of Birth: ").strip()
        if not re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", prompt): sys.exit("Invalid date")
        return prompt

def validate(s):
    today = str(date.today())
    y, m, d = today.split("-")
    y, m, d = int(y), int(m), int(d)
    try:
        year, month, day = s.split("-")
        year, month, day = int(year), int(month), int(day)
        if year < 1 or year > y or month < 1 or month > 12 or day < 1 or day > 31: raise ValueError
        if year == y:
            if month > m: raise ValueError
            if month == m:
                if day > d: raise ValueError
        return [year, month, day]

    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
