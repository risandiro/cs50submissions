import re
import sys

def main():
    print(convert(input("Hours: ").strip()))

def convert(s):
    # if matches := re.search(r"^ (AM|PM) to  (AM|PM)$", s):
    if matches := re.search(r"^([0-9]{1,2}) (AM|PM) to ([0-9]{1,2}) (AM|PM))$", s):
        a, b = matches.group(1), matches.group(2)
        print(a, b)



if __name__ == "__main__":
    main()
