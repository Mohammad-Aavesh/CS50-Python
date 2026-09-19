from pyfiglet import Figlet
from random import choice
import sys

f = Figlet()
if len(sys.argv) == 1:
    fo = choice(f.getFonts())
    f.setFont(font=fo)
    Input = input("Input: ")
    print(f.renderText(Input))
elif len(sys.argv) == 3 and sys.argv[1] in ["-f","--font"]:
    if sys.argv[2] in f.getFonts():
        f.setFont(font=sys.argv[2])
        Input = input("Input: ")
        print(f.renderText(Input))
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

