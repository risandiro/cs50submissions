import re
import sys

def main():
    print(convert(input("Hours: ").strip()))

def convert(s):
    # if matches := re.search(r"^ (AM|PM) to  (AM|PM)$", s):
    if matches := re.search(r"^([0-9]{1,2}) (AM|PM) to ([0-9]{1,2}) (AM|PM)$", s):
        a, b, x, y = matches.group(1), matches.group(2), matches.group(3), matches.group(4)
        print(a, b, x, y, sep="\n")
        return True
    return False
if __name__ == "__main__":
    main()
