import sys
import random
from pyfiglet import Figlet


input = input("Input: ")

if len(sys.argv < 2):
    figlet = Figlet()
    print(figlet)
    figlet.getFonts()
    print(figlet)
    figlet.setFont(font="slant")

    print(figlet.renderText(input))

# if len(sys.argv == 3):

