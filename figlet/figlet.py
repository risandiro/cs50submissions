import sys
import random
from pyfiglet import Figlet

fonts = figlet.getFonts()

input = Figlet(input("Input: "))

input = figlet.setFont(font="coinstak")
print(input)

# if len(sys.argv == 1):

