import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()
input = input("Input: ")
figlet = figlet.setFont(font="coinstak")
print(figlet)

# if len(sys.argv == 1):

