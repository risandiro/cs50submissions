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
            f_h, f_m = first_number.split(":")
            if first_ampm == "PM":
                f_h = int(f_h)
                fh += 12
                f_h = str(f_h)
                first_number = f"{f_h}:{f_m}"
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
