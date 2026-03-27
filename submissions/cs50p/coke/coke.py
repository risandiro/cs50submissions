total = 50
print("Amount Due: 50")

while total > 0:
    coin = input("Insert Coin: ")

    match coin:
        case "25":
            if total >= 0:
                total = total - 25
                if total <= 0:
                    print("Change Owed:", -total)
                else:
                    print("Amount Due:", total)
        case "10":
            if total >= 0:
                total = total - 10
                if total <= 0:
                    print("Change Owed:", -total)
                else:
                    print("Amount Due:", total)
        case "5":
            if total >= 0:
                total = total - 5
                if total <= 0:
                    print("Change Owed:", total)
                else:
                    print("Amount Due:", total)

        case _:
            print("Amount Due:", total)
            coin = input("Insert Coin: ")

