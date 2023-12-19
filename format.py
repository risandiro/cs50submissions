import re

name = input("What's your name? ").strip()

# walrus operator if you want to first assign a value and then use it in boolean expression
# using brackets to capture the outputting values
if matches := re.search(r"^(.+), *(.+)$", name):
    # last, first = matches.groups()
    name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")
