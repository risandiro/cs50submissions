import re
import sys

def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    if matches := re.search(r"youtube.com/embed/[a-zA-Z0-9]+\"></iframe>$", s)


if __name__ == "__main__":
    main()
