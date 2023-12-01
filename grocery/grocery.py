grocery_list = {}

while True:
    try:
        item = input()
        if item in grocery_list:
            grocery_list[item] = grocery_list[item] + 1
        else:
            grocery_list[item] = 1
    except EOFError:
        for article, count in grocery_list.items():
            print(count, article.upper())
        break

