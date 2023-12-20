import re
import sys

def main():
    print(convert(input("Hours: ").strip()))

def convert(s):
    # if matches := re.search(r"^ (AM|PM) to  (AM|PM)$", s):
    if matches := re.search(r"^[0-9]| $, s):
        return True
    else:
        raise ValueError


if __name__ == "__main__":
    main()
