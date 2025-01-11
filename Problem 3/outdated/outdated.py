import sys

date = []
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

def main():
    while True:
        str = input("Date: ")
        if validate_date(str):
            if(len(date) != 0):
                sys.exit(convert_to_iso8601(date))

def validate_date(date_str):
    parts = date_str.split()
    if len(parts) == 3:
        month, day, year = parts
        if month in months:
            day = day.rstrip(",")
            month = months.index(month) + 1
            if day.isdigit():
                day = int(day)
                if day < 1 or day > 31:
                    return False
        else:
            return False

    elif len(parts) == 1:
        parts = parts[0].split("/")
        month, day, year = parts

        if month.isdigit():
            month = int(month)
            if month < 1 or month > 12:
                return False
        else:
            return False

        if day.isdigit():
            day = int(day)
            if day < 1 or day > 31:
                    return False
        else:
            return False

        if not year.isdigit():
            return False
    else:
        return False

    add_date(month, day, year)
    return True

def add_date(month, day, year):
    date.append(month)
    date.append(day)
    date.append(year)

def convert_to_iso8601(date_str):
    month, day, year = date_str
    month = int(month)
    day = int(day)

    return f"{year}-{month:02}-{day:02}"

if __name__ == "__main__":
    main()
