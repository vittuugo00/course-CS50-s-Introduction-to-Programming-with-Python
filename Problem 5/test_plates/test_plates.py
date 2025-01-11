from plates import is_valid

def main():
    test_one()
    test_two()
    test_three()
    test_four()
    test_five()

def test_one():
    assert is_valid("CS50") == True

def test_two():
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False

def test_three():
    assert is_valid("PI3.14") == False
    assert is_valid("123ABC") == False

def test_four():
    assert is_valid("H") == False
    assert is_valid("123") == False

def test_five():
    assert is_valid("OUTATIME") == False

if __name__ == "__main__":
    main()