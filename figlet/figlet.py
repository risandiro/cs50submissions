import sys
import random

from pyfiglet import Figlet

input = input("Input: ")
figlet = Figlet(input)
fonts = figlet.getFonts()
print(figlet)

# if len(sys.argv == 1):

