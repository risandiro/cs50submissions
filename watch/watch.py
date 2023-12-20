import re
import sys

def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    if matches := re.search(r"^<iframe .+ src=\"https?://(?:www.)?youtube.com/embed/[a-zA-Z0-9]+\".+></iframe>$", s):
        return True
    return False

if __name__ == "__main__":
    main()
