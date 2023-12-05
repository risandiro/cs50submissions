import sys
from random import shuffle
from pyfiglet import Figlet


input = input("Input: ")

if len(sys.argv) == 1:
    fonts = Figlet()
    fonts = fonts.getFonts()
    shuffle(fonts)

    x = Figlet()
    x.getFonts()
    x.setFont(font = fonts[0])
    print(x.renderText(input))

elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        x = Figlet()
        x.getFonts()
        x.setFont(font = sys.argv[2])
        print(x.renderText(input))

