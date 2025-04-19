def main():
    frac = input("Fraction: ")
    perc = convert(frac)
    output = gauge(perc)

    if output.isnumeric():
        print(f"{output}%")
    else:
        print(output)

def convert(fraction):
    x, y = fraction.split("/")
    if y == "0":
        raise ZeroDivisionError
    if int(y) >= int(x):
        return int(round(int(x) / int(y) * 100))
    else:
        raise ValueError

def gauge(percentage):
    if int(percentage) < 2:
        return "E"

    elif int(percentage) > 98:
        return "F"

    return f"{percentage}%"


if __name__ == "__main__":
    main()
