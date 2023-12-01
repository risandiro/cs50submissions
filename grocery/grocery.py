grocery_list = {}

while True:
    try:
        item = input()
        if item in grocery_list:
            grocery_list[item] = grocery_list[item] + 1
        else:
            grocery_list[item] = 1
    except EOFError:
        for article in grocery_list:
            print(grocery_list[article], grocery_list.keys())


