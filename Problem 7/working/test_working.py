from working import convert
import pytest

def main():
    test_twelve_format()
    test_twentyfour_format()
    test_wrong_format()

def test_twelve_format():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_twentyfour_format():
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
    with pytest.raises(ValueError):
        convert("13:00 to 17:00")

def test_wrong_format():
     with pytest.raises(ValueError):
        convert("9:60 AM to 5:60")
     with pytest.raises(ValueError):
        convert("10:30 PM 8:50 AM")
     with pytest.raises(ValueError):
        convert("7:30 AM 20:50 PM")

if __name__ == "__main__":
    main()
