from numb3rs import validate

def main():
    test_correct_ips()
    test_invalid_ips()

def test_correct_ips():
    assert validate("255.255.255.255") == True
    assert validate("222.99.1.100") == True
    assert validate("1.2.3.4") == True
    assert validate("11.22.33.44") == True

def test_invalid_ips():
    assert validate("cat") == False
    assert validate("275.111.22.3") == False
    assert validate("1.33.275.222") == False
    assert validate("11.222.3.275") == False
    assert validate("111.275.22.3") == False

if __name__ == "__main__":
    main()
