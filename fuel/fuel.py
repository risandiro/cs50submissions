while True:
    try:
        x, y = input("Fraction: ").split("/")
        x , y = int(x), int(y)
        if y >= x:
            percent = int(x / y * 100)
            if percent <= 1:
                print("E")
                break
            elif percent >= 99:
                print("F")
                break
            else:
                print(f"{percent}%")
                break

    except (ValueError, ZeroDivisionError):
        pass
