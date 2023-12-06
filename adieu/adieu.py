name_list = []

while True:
    try:
        name = input("Name: ")
        name_list.append(name)
    except EOFError:
        if len(name_list) == 1:
            print("Adieu, adieu, to", name_list[0])
            break

        elif len(name_list) == 2:
            print(f"Adieu, adieu, to {name_list[0]} and {name_list[1]}")
            break

        elif len(name_list) > 2:
            print("Adieu, adieu, to ", sep="", end="")
            for person in name_list:
                print(person, sep=",", end="")
