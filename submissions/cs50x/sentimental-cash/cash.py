total = 0


def main():
    while True:
        try:
            change = float(input("Change: "))
            if change < 0:
                raise
            break

        except:
            continue

    pennies(nickels(dimes(quarters(change))))
    print(total)


def quarters(n: float) -> float:
    global total
    while n >= 0.25:
        n -= 0.25
        total += 1
    return round(n, 2)


def dimes(n: float) -> float:
    global total
    while n >= 0.10:
        n -= 0.10
        total += 1
    return round(n, 2)


def nickels(n: float) -> float:
    global total
    while n >= 0.05:
        n -= 0.05
        total += 1
    return round(n, 2)


def pennies(n: float) -> float:
    global total
    while n >= 0.01:
        n -= 0.01
        total += 1
    return


main()
