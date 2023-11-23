total = 50
coin = input("Insert Coin: ")

while total <= 0
    match coin:
        case "25":
            if total != 0:
                total = total - 25
                print("Amount Due:", total)
        case "10":
            if total != 0:
                total = total - 10
                print("Amount Due:", total)
        case "5":
            if total != 0:
                total = total - 5
                print("Amount Due:", total)
