import re
import sys

def main():
    print(convert(input("Hours: ").strip()))

def convert(s):
    # if matches := re.search(r"^ (AM|PM) to  (AM|PM)$", s):
    if matches := re.search(r"^([0-9]{1,2})(?::[0-9]{2})? (AM|PM) to ([0-9]{1,2})(?::[0-9]{2})? (AM|PM)$", s):
        a, b, x, y = matches.groups()
        a, b, x, y = int(a), int(b), int(x), int(y)
        print(a, b, c, d, sep="\n")
    else:
        raise ValueError


if __name__ == "__main__":
    main()
