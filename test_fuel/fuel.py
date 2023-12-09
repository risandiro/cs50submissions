def main():



def convert(fraction):
    x, y = fraction.split("/")
    x , y = int(x), int(y)
    if y >= x:
        return int(round(x / y * 100))

def gauge(percentage):
    if percentage <= 1:
        return "E"
                    break
                elif percent >= 99:
                    print("F")
                    break
                else:
                    print(f"{percent}%")
                    break
