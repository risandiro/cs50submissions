grocery_list = {}

while True:
    try:
        item = input().lower()
        if item in grocery_list:
            grocery_list[item] = grocery_list[item] + 1
        else:
            grocery_list[item] = 1
    except EOFError:
        print("")
        keys = list(grocery_list.keys())
        print(keys, "\n")
        keys.sort()
        print(keys, "\n")
        grocery_list = {i: grocery_list[i] for i in keys}

        for article, count in grocery_list.items():
            print(count, article.upper())
        break

