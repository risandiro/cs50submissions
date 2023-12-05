import sys
import random
from pyfiglet import Figlet


input = input("Input: ")

if len(sys.argv == 1):
    figlet = Figlet()
    figlet.getFonts()
    figlet.setFont(font="slant")

    print(figlet.renderText(input))

if len(sys.argv == 3):
    
