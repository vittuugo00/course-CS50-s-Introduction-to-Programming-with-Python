from um import count

def main():
    test_one()
    test_two()
    test_three()

def test_one():
    assert count("Um, thanks, um...") == 2

def test_two():
    assert count("Um, thanks for the album") == 1

def test_three():
    assert count("cat") == 0

if __name__ == "__main__":
    main()