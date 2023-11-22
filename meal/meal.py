def main():
    x = convert(input("What time is it? "))
    


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    hours  = hours + (minutes / 60)
    return hours

if __name__ == "__main__":
    main()
