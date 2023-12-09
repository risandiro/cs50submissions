def main():
    frac = input("Fraction: ")
    perc = convert(frac)
    output = gauge(perc)
    if output 

def convert(fraction):
    x, y = fraction.split("/")
    x , y = int(x), int(y)
    if y >= x:
        return int(round(x / y * 100))

def gauge(percentage):
    if percentage <= 1:
        return "E"

    elif percent >= 99:
        return "F"

    else:
        return f"{percent}%"


if __name__ == "__main__":
    main()
