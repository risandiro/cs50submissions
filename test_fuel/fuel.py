def main():



def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            x , y = int(x), int(y)
            if y >= x:
                return int(round(x / y * 100))
        except (ValueError, ZeroDivisionError):
            pass


                if percent <= 1:
                    print("E")
                    break
                elif percent >= 99:
                    print("F")
                    break
                else:
                    print(f"{percent}%")
                    break
