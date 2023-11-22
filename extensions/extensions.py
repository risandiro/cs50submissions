x = input("File name: ")
x = x.name.strip()
x = x.lower()

if x.endswith(".gif" or ".jpg" or ".jpeg" or ".png" or ".pdf" or ".txt" or ".zip") == True:
    match x:
        case ".gif"

else:
    print("application/octet-stream")

