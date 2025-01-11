from datetime import date
import sys
import re
import inflect

p = inflect.engine()

class Birth:
    def __init__(self, birth):
        if date := re.search(r"^([0-9]{4})-([0-9]{2})-([0-9]{2})$", birth):
            self.year  = int(date.group(1))
            self.month = int(date.group(2))
            self.day   = int(date.group(3))
        else:
            sys.exit("Invalid date")

    @classmethod
    def get(cls):
        birth = input("Date of Birth: ")
        return cls(birth)

def main():
    try:
        birth = Birth.get()
        print(mins_alive(birth).capitalize(), "minutes")
    except:
        sys.exit("Invalid date")


def mins_alive(birth):
    birth_date = date(birth.year, birth.month, birth.day)
    time_alive = date.today() - birth_date
    minutes = (time_alive.days * 24 * 60)
    words = p.number_to_words(minutes, andword="")
    return words


if __name__ == "__main__":
    main()