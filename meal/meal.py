def main():
    x = convert(input("What time is it? "))
    if 7 <= x <= 8:
        print("breakfast time")
    elif 12 <= x <= 13:
        print("lunch time")
    elif 18 <= x <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
        if 0 <= hours <= 24
    hours  = hours + (minutes / 60)
    return hours

if __name__ == "__main__":
    main()
