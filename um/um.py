import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    re.findall(r"\bum\b" , s)



if __name__ == "__main__":
    main()
