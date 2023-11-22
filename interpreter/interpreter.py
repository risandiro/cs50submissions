expression = input("Expression: ")
x, y, z = expression.split(" ")
x = int(x)
z = int(z)

match y:
    case "+":
        print(x + z)
    case "-":
        print(x - z)
    case "*":
        print(x * z)
    case "/":
        
        print(x / z)
