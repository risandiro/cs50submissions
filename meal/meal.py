def main():
    x = input("What time is it? ")
    convert(x)


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
     = hours + (minutes / 60)

if __name__ == "__main__":
    main()
