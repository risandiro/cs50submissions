import sys, re, inflect
from datetime import date

def main():
    user_input = input("Date of Brith: ")
    user_input = validate(user_input)
    user_input = minutes(user_input)
    print(time_to_words(user_input))



def validate(inp):
    current = str(date.today())
    c_year, c_month, c_day = current.split("-")
    c_year, c_month, c_day = int(c_year), int(c_month), int(c_day)

    try:
        if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", inp):
            year, month, day = inp.split("-")
            year, month, day = int(year), int(month), int(day)

            if year > c_year:
                 raise ValueError
            if year == c_year and month > c_month:
                 raise ValueError
            if year == c_year and month == c_month and day > c_day:
                raise ValueError

            user_input = date(year, month, day)
            return user_input

        else:
            raise ValueError

    except ValueError:
        sys.exit("Invalid date")


def minutes(inp):
    current = date.today()
    time = current - inp
    return int(time.days)

def time_to_words(inp):
    p = inflect.engine()
    words = p.number_to_words(inp)
    words = words.capitalize() + " minutes"
    words = words.replace("and", None)
    return words


if __name__ == "__main__":
    main()
