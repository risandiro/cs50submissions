def main():
    number = input("Number: ")

    if verify(number) != True:
        print("INVALID")

    if len(number) == 13 and number[0] == 4:
        print("VISA")

    elif len(number) == 15 and number[0] == 3 and number[1] == 4 or number[1] == 7:
        print("AMEX")

    elif len(number) == 16:
        if number[0] == 4:
            print("VISA")
        elif number[0] == 5 and number[1] in [1, 2, 3, 4, 5]:
            print("MASTERCARD")
    else:
        print("INVALID")


def verify(card):
    list = []
    for digid in card[::-2]:
        try:
            list.append(int(digid) * 2)
        except:
            return False

    sum = 0
    for i in list:
        if i < 10:
            sum =+ sum

        if i >= 10:
            sum =+ sum % 10
            sum =+ 1

    if sum % 10 == 0:
        return True
    else:
        return False


main()
