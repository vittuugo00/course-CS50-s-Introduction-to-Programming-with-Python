import sys

def main():
    check_commandline()
    try:
        lines = open_file() #return the lines of the file
        print(count_lines(lines))
    except FileNotFoundError:
        sys.exit("File does not exist")

def check_commandline():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not (sys.argv[1].endswith(".py")) or sys.argv[1] == "py":
        sys.exit("Not a python file")

def open_file():
    with open(sys.argv[1]) as file:
        lines = file.readlines()
        return lines

def count_lines(lines):
    count = 0
    for line in lines:
        line = line.lstrip()
        if not line.startswith("#") and not line.startswith("\n") and not line == "":
            count = count + 1
    return count

if __name__ == "__main__":
    main()
