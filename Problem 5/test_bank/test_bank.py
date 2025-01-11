from bank import value

def main():
    test_hello()
    test_hi()
    test_whatsup()

def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0

def test_hi():
    assert value("hi") == 20

def test_whatsup():
    assert value("What's up?") == 100

if __name__ == "__main__":
    main()