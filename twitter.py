url = input("URL: ").strip()

# string.replace(find, replace)
username = url.replace("https://twitter.com/", "")
print(username)
