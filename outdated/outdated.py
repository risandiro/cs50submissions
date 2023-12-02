months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")
        x, y, z = date.split("/")

    except ValueError:
        month_date, year = date.split(",")
        month, day = month_date.split(" ")
        year = year.strip()
        if month in months:
            month_index = 0
            for x in months:
                if(x == month):
                    break
                month_index += 1

            try:
                year = int(year)
                print(year, month_index, day, sep="-")

            except ValueError:


