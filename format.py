import re

name = input("What's your name? ").strip()

# using brackets to capture the outputting values
matches = re.search(r"^(.+), ?(.+)$", name)
if matches:
    # last, first = matches.groups()
    name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")
