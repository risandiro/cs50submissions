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
        balance -= temp * 0.25
        total += temp

    if balance >= 0.10:
        int = balance // 0.10
        balance -= temp * 0.10
        total += temp

    if balance >= 0.05:
        int = balance // 0.05
        balance -= temp * 0.05
        total += temp


    print(total + balance)

main()
