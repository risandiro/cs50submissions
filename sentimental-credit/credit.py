def main():
    number = input("Number: ")

    if verify(number) != True:
        print("INVALID")
        return 1
    print("good")




def verify(card):
    list = []
    for digid in card[::-1]:
        list.append(digid * 2)

    sum = 0
    for i in list:
        if int(i) < 10:
            sum =+ sum

        if int(i) >= 10:
            sum =+ sum % 10
            sum =+ 1

    if sum % 10 == 0:
        return True
    else:
        return False

main()
