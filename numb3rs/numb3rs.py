import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    try:
        a, b, c, d = ip.split(".")
        a, b, c, d = int(a), int(b), int(c), int(d)
        if 0 >= a <= 255 and 0 >= b <= 255 and 0 >= c <= 255 and 0 >= d <= 255:
            return True
        return False
    except ValueError:
       return False


if __name__ == "__main__":
    main()
