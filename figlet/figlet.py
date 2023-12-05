import sys
from random import shuffle
from pyfiglet import Figlet


x = Figlet()
x.getFonts()
input = input("Input: ")

if len(sys.argv) == 1:
    fonts = Figlet()
    fonts = fonts.getFonts()
    shuffle(fonts)

    x.setFont(font = fonts[0])
    print(x.renderText(input))

elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        x.setFont(font = sys.argv[2])
        print(x.renderText(input))

