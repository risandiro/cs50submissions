import re
import sys

def main():
    print(convert(input("Hours: ").strip()))

def convert(s):
    if matches := re.search(r"^xx (AM|PM) to xx (AM|PM)$", s):
        return True
    return False



if __name__ == "__main__":
    main()


([0-9]|(10|11|12))     (:[0-6][0-9])?
