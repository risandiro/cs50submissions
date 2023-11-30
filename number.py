"""

try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

# without else function, x never gets defined if input is not an integer, because
# the program is executed from right to left and when we get to the input conversion
# into the integer, it creates a value error and jumps straight to exception without
# ever getting to defining the x

"""

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x?"))
        except ValueError:
            print("x is not an integer")
        else:
            # return works as a break from a loop and also finishes the definition
            return x


main()
