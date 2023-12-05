import sys
from random import shuffle
from pyfiglet import Figlet


input = input("Input: ")
fonts = Figlet()
fonts = fonts.getFonts()
shuffle(fonts)
print(fonts)

'''
if len(sys.argv) == 1:
    x = Figlet()
    x.getFonts()
    x.setFont(font="fonts")
    print(x.renderText(input))

elif len(sys.argv == 3):
'''

