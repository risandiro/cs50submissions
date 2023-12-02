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
        month, day, year = date.split("/")
        if month.isnumeric() and day.isnumeric() and year.isnumeric():
            day, month = int(day), int(month)
            if 0 < day <= 31 and 0 < month <= 12:

                if day <= 9:
                    day = str(day)
                    add = "0"
                    day = f"{add}{day}"
                if month <= 9:
                    month = str(month)
                    add = "0"
                    month = f"{add}{month}"
                print(year, month, day, sep="-")
                break


    except ValueError:
        try:
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
                            add = "0"
                            month_index = f"{add}{month_index}"

                        print(year, month_index, day, sep="-")
                        break

        except ValueError:
