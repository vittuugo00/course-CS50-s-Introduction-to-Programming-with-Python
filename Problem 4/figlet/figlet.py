from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

def main():
    if len(sys.argv) <= 1:
        f = random_font()
        figlet.setFont(font=f)
        print(figlet.renderText(get_text()))
    else:
        check_font()
        font = (f"{sys.argv[2]}")
        figlet.setFont(font=font)
        print(figlet.renderText(get_text()))

def random_font():
    return random.choice(figlet.getFonts())

def get_text():
    return input("input: ")

def check_font():
    if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and (sys.argv[2] in figlet.getFonts()):
        print("")
    else:
        sys.exit("Something goes wrong, try again")


main()
