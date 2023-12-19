import re

url = input("URL: ").strip()

# string.replace(find, replace)
username = url.replace("https://twitter.com/", "")

# string.removeprefix(removes a prefix but leaves alone if it doesn't start with prefix)
username = url.removeprefix("https://twitter.com/")

re.sub(pattern, repl, string, count=0, flags=0)





print(username)
