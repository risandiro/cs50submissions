import re

name = input("What's your name? ").strip()

# using brackets to capture the outputting values
matches = re.search(r"^(.+),(.+)$", name)
if matches:
    # last, first = matches.groups()
    last = matches.group(1)
    first = matches.group(2)

    name = f"{first} {last}"

print(f"hello, {name}")
