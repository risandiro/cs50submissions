def main():
    while True:
        try:
            change = float(input("Change: "))
            if change < 0:
                raise
            break

        except:
            continue

    total = 0
    balance = change

    if change > 0.25:
        total += balance / 0.25
        balance = balance % 0.25



main()
