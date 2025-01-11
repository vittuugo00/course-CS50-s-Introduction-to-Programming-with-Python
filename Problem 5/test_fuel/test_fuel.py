from fuel import convert, gauge
import pytest

def main():
    test_convert()
    test_convert_raises()
    test_gauge()

def test_convert():
    assert convert("3/4") == 75
    assert convert("0/4") == 0

def test_convert_raises():
    with pytest.raises(ValueError):
        convert("7/4")

    with pytest.raises(ZeroDivisionError):
        convert("5/0")

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(79) == "79%"

if __name__ == "__main__":
    main()
