import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# outputs a slice of the list, starting from 1 to the end
# using a negative number slices the list from the other side
for arg in sys.argv[1:-1]:
    print("hello, my name is", arg)
