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
        grocery_list = list(grocery_list.keys())
        grocery_list.sort()
        grocery_list = {i: grocery_list[i] for i in grocery_list}
        for article, count in grocery_list.items():
            print(count, article.upper())
        break

