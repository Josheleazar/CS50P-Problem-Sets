import random
import sys
from pyfiglet import Figlet
figlet = Figlet()
fts = figlet.getFonts()

if len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fts:
    s = input("Input: ")
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(s))
else:
    sys.exit("Try again")