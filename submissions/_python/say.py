# pip install cowsay
import cowsay
import sys

# only takes one string as a argument
if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])
