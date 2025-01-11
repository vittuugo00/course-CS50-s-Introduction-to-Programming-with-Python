import sys
import csv

def main():
    write_after(open_before())

def check_commandline():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not (sys.argv[1].endswith(".csv")) or not (sys.argv[2].endswith(".csv")):
        sys.exit("Not a CSV file")

def open_before():
    check_commandline()
    scourgify = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                scourgify.append(row)
        return scourgify
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

def write_after(scourgify):
    with open(sys.argv[2], 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in scourgify[1:]:
            last, first = row[0].split()
            last = last.rstrip(",")
            house = row[1]
            writer.writerow({"first": first, "last": last, "house": house})

if __name__ == "__main__":
    main()
