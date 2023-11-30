while True:
    try:
        x, y = input("Fraction: ").split("/")
        x , y = int(x), int(y)
        percent = x / y * 100
        if percent <= 1:
            print("E")
        elif percent >= 99:
            print("F")
        else:
            print(f"{int(percent)}")

        break

    except (ValueError, ZeroDivisionError):
        pass

    except (percent > 100):
        pass





