name_list = []

while True:
    try:
        name = input("Name: ")
        name_list.append(name)
    except EOFError:
        if len(name_list)
