import re


def main():
    try:
        print(convert(input("Hours: ")))
    except:
        raise ValueError("Invalid input format. Please use '9:00 AM to 5:00 PM' format.")

def convert(s):
    time = re.match(r"^(\d+)(?::(\d*))?\s+(AM|PM)\s*to\s*(\d+)(?::(\d*))?\s+(AM|PM)$", s, re.IGNORECASE)
    try:
        if time_isvalid(time.groups()):
            hour_one, min_one, am_pm_one, hour_two, min_two, am_pm_two = time.groups()
    except:
        raise ValueError("Invalid input format. Please use '9:00 AM to 5:00 PM' format.")

    if min_one == None:
        min_one = "00"
    if min_two == None:
        min_two = "00"

    if am_pm_one == "PM":
        if hour_one != "12":
            hour_one = int(hour_one) + 12
    elif am_pm_two == "PM":
        if hour_two != "12":
            hour_two = int(hour_two) + 12

    if am_pm_one == "AM" and hour_one == "12":
        hour_one = "00"
    if am_pm_two == "AM" and hour_two == "12":
        hour_two = "00"

    return print_time(hour_one, hour_two, min_one, min_two)

def time_isvalid(time):
    hour_one, min_one, am_pm_one, hour_two, min_two, am_pm_two = time

    if min_one == None:
            min_one = "00"
    if min_two == None:
        min_two = "00"

    if int(hour_one) <= 12 and int(min_one) < 60 and int(hour_two) <= 12 and int(min_two) < 60:
        return True

    raise ValueError("Invalid time.")

def print_time(hour_start, hour_end, minu_start, minu_end):
    hour_start = int(hour_start)
    hour_end = int(hour_end)

    return f"{hour_start:02d}:{minu_start:02} to {hour_end:02d}:{minu_end:02}"


if __name__ == "__main__":
    main()
