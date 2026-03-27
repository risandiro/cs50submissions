expression = input("Expression: ")
x, y, z = expression.split(" ")
x = int(x)
z = int(z)

match y:
    case "+":
        print(float(x + z))
    case "-":
        print(float(x - z))
    case "*":
        print(float(x * z))
    case "/":
        if z == 0:
            print("infinity")
        else:
            print(float(x / z))
