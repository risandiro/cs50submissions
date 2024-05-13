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

    if balance >= 0.25:
        temp = balance // 0.25
        balance = balance % 0.25

    if balance >= 0.10:
        total += balance // 0.10
        balance = balance % 0.10

    if balance >= 0.5:
        total += balance // 0.05
        balance = balance % 0.05

    print(total + balance)

main()
