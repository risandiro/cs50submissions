import sys
from random import shuffle
from pyfiglet import Figlet


input = input("Input: ")
fonts = Figlet()
fonts = fonts.getFonts()
shuffle(fonts)


if len(sys.argv) == 1:
    x = Figlet()
    x.getFonts()
    x.setFont(font = fonts[1])
    print(x.renderText(input))

# elif len(sys.argv == 3):

