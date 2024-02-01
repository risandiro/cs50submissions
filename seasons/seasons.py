import sys, re, inflect
from datetime import date

def main():
    '''
    today = str(date.today())
    y, m, d = today.split("-")
    y, m, d = int(y), int(m), int(d)
    '''
    y, m, d = 2000, 1, 1

    yy_mm_dd = validate(get_date())
    yy, mm, dd = yy_mm_dd[0], yy_mm_dd[1], yy_mm_dd[2]

    yir = (y - yy) * 525960
    mont = (m - mm) * 43800
    dej = (d - dd) * 1440
    print(yir + mont + dej)



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
