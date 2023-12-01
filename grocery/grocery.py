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
        # copy all keys from a dictionary to a new list
        keys.sort()
        # sort the list alphabetically
        grocery_list = {i: grocery_list[i] for i in keys}
        # copy the i value from the list and replace it with i key in the dic

        for article, count in grocery_list.items():
            print(count, article.upper())
        break

