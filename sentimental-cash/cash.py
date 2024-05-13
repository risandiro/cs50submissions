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
        
    dimes(change)
    print(total)


def dimes(n: float):
    while n >= 0.25:
        n - 0.25
        total += 1
    return n


main()
