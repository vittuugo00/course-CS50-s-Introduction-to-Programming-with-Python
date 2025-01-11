import sys
import csv
from tabulate import tabulate

def main():
    print_tabulate(create_menu())

def check_commandline():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not (sys.argv[1].endswith(".csv")):
        sys.exit("Not a CSV file")

def create_menu():
    check_commandline()
    menu = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                menu.append(row)
        return menu
    except FileNotFoundError:
        sys.exit("File does not exist")

def print_tabulate(menu):
    print(tabulate(menu[1:], menu[0], tablefmt="grid"))

if __name__ == "__main__":
    main()
