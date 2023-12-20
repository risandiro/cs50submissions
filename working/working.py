import re
import sys

def main():
    print(convert(input("Hours: ").strip()))

def convert(s):
    # if matches := re.search(r"^ (AM|PM) to  (AM|PM)$", s):
    if matches := re.search(r"^([0-9]{1,2}(?::[0-9]{2})?) (AM|PM) to ([0-9]{1,2}(?::[0-9]{2})?) (AM|PM)$", s):
        first_time, second_time, x, y = matches.groups()
        if ":" in first_time:
            first_time_hours, first_time_seconds = first_time.split(":")
            if first_time_hours



    else:
        raise ValueError


if __name__ == "__main__":
    main()
