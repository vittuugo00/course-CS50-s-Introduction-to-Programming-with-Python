from seasons import mins_alive
from datetime import date

def main():
    test_birth_date()


def test_birth_date():
    assert mins_alive(date(2000, 6, 15)) == "twelve million, one hundred forty-seven thousand, eight hundred forty"

if __name__ == "__main__":
    main()