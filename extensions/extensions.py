x = input("File name: ")
x = x.name.strip()
x = x.lower()

if x.endswith(".gif"):
    print("image/gif")
elif x.endswith(".jpg" or ".jpeg"):
    print("image/jpeg)
elif x.endswith(".png"):
    print("image/png")



