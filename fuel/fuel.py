while True:
    try:
        x, y = input("Fraction: ").split("/")
        x , y = int(x), int(y)
        break

    except (ValueError, ZeroDivisionError):
        pass

print(f"{int(x / y * 100)}%")

