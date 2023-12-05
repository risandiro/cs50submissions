#   docs.python.org/3/library/sys.html
import sys

try:
    # sys.argv[0] is "name.py"
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
