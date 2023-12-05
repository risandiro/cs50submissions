'''

#   docs.python.org/3/library/sys.html
import sys

if len(sys.argv) < 2:
    # len 1 is the name of the program, len 2 is the expected input
    sys.exit("Too few arguments")

if len(sys.argv) > 2:
    # len 1 is the name of the program, len 2 is the expected input
    sys.exit("Too many arguments")

# sys.argv[0] is "name.py"
print("hello, my name is", sys.argv[1])

# if a input is queted, it's recognized as a single string, even if there's a space between them

'''

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# outputs a slice of the list, starting from 1 to the end
# using a negative number slices the list from the other side
for arg in sys.argv[1:-1]:
    print("hello, my name is", arg)
