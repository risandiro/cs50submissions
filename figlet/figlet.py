import sys
import random
from pyfiglet import Figlet


input = input("Input: ")

if len(sys.argv == 1):
    figlet = Figlet()
    print(figlet)
    figlet.getFonts()
    figlet.setFont(font=)

    print(figlet.renderText(input))

if len(sys.argv == 3):

