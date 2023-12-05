import sys
import random

from pyfiglet import Figlet

fonts = figlet.getFonts()
input = input("Input: ")

if len(sys.argv) == 1:
    figlet = Figlet(input)

# if len(sys.argv == 3):

