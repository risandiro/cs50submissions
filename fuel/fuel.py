while True:
    try:
        return int(input("Fraction: "))
    except (ValueError, ZeroDivisionError):
        pass
