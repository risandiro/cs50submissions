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
            index = 0
            for month in months:
                if(month == months):
                    break


