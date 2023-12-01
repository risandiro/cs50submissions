menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}

total = 0
while True:
    try:
        item = input("Item: ")
        if item in menu:
            total = total + menu[item]
            total = round(total, 2)
            print(f"Total: ${total:.2f}")

# if user inputs control-d, which is a common way of ending one's input
    except EOFError:
        print("")
        break
