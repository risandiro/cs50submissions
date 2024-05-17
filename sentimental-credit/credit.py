def verify(card):

    list = []
    for digid in card[::-2]:
        list.append(digid * 2)

    sum = 0
    for i in list:
        if i < 10:
            sum =+ sum

        if i >= 10
            x = sum % 10



