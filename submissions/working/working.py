import re
import sys

def main():
    print(convert(input("Hours: ").strip()))

def convert(s):
    if matches := re.search(r"^((?:[1-9]|10|11)(?::[0-5][0-9])?|12(?::00)?) (AM|PM) to ((?:[1-9]|10|11)(?::[0-5][0-9])?|12(?::00)?) (AM|PM)$", s):
        first_number = matches.group(1)
        first_ampm = matches.group(2)
        second_number = matches.group(3)
        second_ampm = matches.group(4)


        f_m = None
        if ":" in first_number:
            first_number, f_m = first_number.split(":")

        first_number = int(first_number)
        if first_ampm == "PM":
            first_number += 12


        if first_number <= 10:
            first_number = str(first_number)
            first_number = f"0{first_number}"
        else:
            first_number = str(first_number)


        if first_ampm == "AM":
            if first_number == "12":
                first_number = "00"

        elif first_number == "24":
            first_number = "12"


        if f_m:
            first_number = f"{first_number}:{f_m}"
        else:
            first_number = f"{first_number}:00"


        s_m = None
        if ":" in second_number:
            second_number, s_m = second_number.split(":")

        second_number = int(second_number)
        if second_ampm == "PM":
            second_number += 12


        if second_number <= 10:
            second_number = str(second_number)
            second_number = f"0{second_number}"
        else:
            second_number = str(second_number)


        if second_ampm == "AM":
            if second_number == "12":
                second_number = "00"

        elif second_number == "24":
                second_number = "12"


        if s_m:
            second_number = f"{second_number}:{s_m}"
        else:
            second_number = f"{second_number}:00"


        return f"{first_number} to {second_number}"

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
