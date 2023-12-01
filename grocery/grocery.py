grocery_list = {}

while True:
    try:
        item = input()
        if item in grocery_list:
            grocery_list[item] = grocery_list[item] + 1
        else:
            grocery_list[item] = 0
    except EOFError:
        print(grocery_list)
        break
