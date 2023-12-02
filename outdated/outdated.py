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
            month_index += 1

            if year.isnumeric() and day.isnumeric():
                day = int(day)
                if 0 < day <= 31:
                    if day <= 9:
                        day = str(day)
                        add = "0"
                        day =  f"{add}{day}"

                    if month_index <= 9:
                        month_index = 0 + month_index

                    print(year, month_index, day, sep="-")



