import re
import sys

def main():
    print(convert(input("Hours: ").strip()))

def convert(s):
    if matches := re.search(r"^(([1-9]|10|11)(:[0-5][0-9])?|12(:00)?) (AM|PM) to (([1-9]|10|11)(:[0-5][0-9])?|12(:00)?) (AM|PM)", s):
        first_number = matches.group(1)
        first_ampm = matches.group(5)
        second_number = matches.group(6)
        print(first_number, second_number, first_ampm, sep="\n")
        return True
    else:
        raise ValueError


if __name__ == "__main__":
    main()


# (([1-9]|10|11)(:[0-5][0-9])?|12(:00)?)

# ([1-9]|10|11)
# (:[0-5][0-9])?
# 12(:00)?
