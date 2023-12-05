import sys
import random
from pyfiglet import Figlet


input = input("Input: ")
fonts = Figlet()
fonts = fonts.getFonts()
fonts

if len(sys.argv) == 1:
    x = Figlet()
    x.getFonts()
    x.setFont(font="slant")
    print(x.renderText(input))

# elif len(sys.argv == 3):


