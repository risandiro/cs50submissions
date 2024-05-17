def main():
    number = input("Number: ")

    if verify(number) != True:
        print("INVALID")

    if len(number) == 15:
        if 




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
