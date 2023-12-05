import sys
from random import shuffle
from pyfiglet import Figlet


x = Figlet()
x.getFonts()

fonts = Figlet()
fonts = fonts.getFonts()

if len(sys.argv) == 1:
    input = input("Input: ")
    shuffle(fonts)
    x.setFont(font = fonts[0])
    print("Output:\n", x.renderText(input), sep="")

elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in fonts:
            input = input("Input: ")
            x.setFont(font = sys.argv[2])
            print("Output:\n", x.renderText(input), sep="")
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
