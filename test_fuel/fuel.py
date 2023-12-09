def main():
    frac = input("Fraction: ")
    perc = convert(frac)
    output = gauge(perc)

    if output.isnumeric():
        print(f"{output}%")
    else:
        print(output)

def convert(fraction):
    import sys
    x, y = fraction.split("/")
    if y == "0":
        raise ZeroDivisionError
        sys.exit()
    if int(y) >= int(x):
        return int(round(x / y * 100))
    else:
        raise ValueError
        sys.exit()

def gauge(percentage):
    if int(percentage) < 2:
        return "E"

    elif int(percentage) > 98:
        return "F"

    return f"{percentage}%"


if __name__ == "__main__":
    main()
