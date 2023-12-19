import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    try:
        a, b, c, d = ip.split(".")
        return True

    except ValueError:
       return False



if __name__ == "__main__":
    main()
