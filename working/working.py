import re
import sys

def main():
    print(convert(input("Hours: ").strip()))

def convert(s):
    if matches := re.search(r"^(([1-9]|10|11)(:[0-5][0-9])?|12(:00)?) (AM|PM) to (([1-9]|10|11)(:[0-5][0-9])?|12(:00)?) (AM|PM)", s):
        a = matches.group(2)
        print(a)
        return True
    else:
        raise ValueError


if __name__ == "__main__":
    main()


# (([1-9]|10|11)(:[0-5][0-9])?|12(:00)?)

# ([1-9]|10|11)
# (:[0-5][0-9])?
# 12(:00)?
