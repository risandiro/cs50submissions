# move the last item in the list to the beginning

list = [1, 0, 2, 0, 4, 6]
new_list = []
new_list.append(list[-1])

i = 0
for item in list:
    if i + 1 < len(list):
        new_list.append(item)
        i += 1

print(new_list)
