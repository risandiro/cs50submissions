import re

url = input("URL: ").strip()

# string.replace(find, replace)
username = url.replace("https://twitter.com/", "")

# string.removeprefix(removes a prefix but leaves alone if it doesn't start with prefix)
username = url.removeprefix("https://twitter.com/")


# re.sub(pattern, repl, string, count=0, flags=0)

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

print(username)



url = input("URL: ").strip()

if matches := re.search(r"(?:https?://)?(?:www\.)?twitter\.com/[a-z0-9_]", url, re.IGNORECASE)
    print(f"Username:", matches.group(1))

# re.split() allows to split a string on multiple possible characters
# re.
