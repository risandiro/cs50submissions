def main():
    x = input("What time is it? ")
    convert(x)



def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    x  = hours + (minutes / 60)
    return x

if __name__ == "__main__":
    main()
