def main():
    time = input("What time is it? ")
    convert(time)

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    hours = hours + (minutes / 60)
    print(hours)

if __name__ == "__main__":
    main()
