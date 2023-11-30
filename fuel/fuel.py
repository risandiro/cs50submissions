while True:
    try:
        x, y = input("Fraction: ").split("/")
        x , y = int(x), int(y)
        if y >= x:
            percent = round(x / y * 100)
            if percent <= 1:
                print("E")
                break
            elif percent >= 99:
                print("F")
                break
            else:
                print(f"{int(percent)}%")
                break

    except (ValueError, ZeroDivisionError):
        pass
