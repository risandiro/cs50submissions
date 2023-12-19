url = input("URL: ").strip()

# string.replace(find, replace)
# username = url.replace("https://twitter.com/", "")

# string.removeprefix(remove a part of the string and everything before it)
username = url.removeprefix("https://twitter.com/")
print(username)
