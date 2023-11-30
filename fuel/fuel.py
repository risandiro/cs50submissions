while True:
    try:
        x, y = input("Fraction: ").split("/")
        x , y = int(x), int(y)
        break

    except (ValueError, ZeroDivisionError):
        pass

percent = x / y * 100
if percent <= 1:
    print("E")
elif percent >= 99:
    print("F")
else:
    print(int(percent))



