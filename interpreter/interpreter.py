expression = input("Expression: ")
x, z = int(x)
int(z)
x, y, z = expression.split(" ")

match y:
    case "+":
        print(x + z)
