import re
import sys

def main():
    print(convert(input("Hours: ").strip()))

def convert(s):
    if matches := re.search(r"^1?[0-9]", s)



if __name__ == "__main__":
    main()
