import re
import sys

def main():
    print(convert(input("Hours: ").strip()))

def convert(s):
    # if matches := re.search(r"^ (AM|PM) to  (AM|PM)$", s):
    if matches := re.search(r"^[0-9]{1-2} (AM/PM) to $", s):
        return True
    return False



if __name__ == "__main__":
    main()
