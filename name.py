#   docs.python.org/3/library/sys.html
import sys

if len(sys.argv) < 2:
    # len 1 is the name of the program, len 2 is the expected input
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    # sys.argv[0] is "name.py"
    print("hello, my name is", sys.argv[1])

# if a input is queted, it's recognized as a single string, even if there's a space between them

