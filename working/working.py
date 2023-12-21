import re
import sys

def main():
    print(convert(input("Hours: ").strip()))

def convert(s):
    if matches := re.search(r"^((?:[1-9]|10|11)(?::[0-5][0-9])?|12(?::00)?) (AM|PM) to ((?:[1-9]|10|11)(?::[0-5][0-9])?|12(?::00)?) (AM|PM)", s):
        first_number = matches.group(1)
        first_ampm = matches.group(2)
        second_number = matches.group(3)
        second_ampm = matches.group(4)

        if ":" in first_number:
            first_number, f_m = first_number.split(":")
            if first_ampm == "PM":
                first_number = int(f_h)
                first_number += 12
                first_number = str(f_h)
                first_number = f"{first_number}:{f_m}"
        return first_number






    else:
        raise ValueError


if __name__ == "__main__":
    main()


# (r"^((?:[1-9]|10|11)(?::[0-5][0-9])?|12(?::00)?) (AM|PM) to ((?:[1-9]|10|11)(?::[0-5][0-9])?|12(?::00)?) (AM|PM)", s):
# (r"^(([1-9]|10|11)(:[0-5][0-9])?|12(:00)?) (AM|PM) to (([1-9]|10|11)(:[0-5][0-9])?|12(:00)?) (AM|PM)", s):
# (([1-9]|10|11)(:[0-5][0-9])?|12(:00)?)

# ([1-9]|10|11)
# (:[0-5][0-9])?
# 12(:00)?
