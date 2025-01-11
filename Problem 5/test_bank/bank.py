def main():
    str = input("Greeting: ").lower()
    print(f"${value(str)}")

def value(str):
    if (str.find("hello", 0, 5) != -1):
        return (0)
    elif (str.find("h", 0, 1) != -1):
        return (20)
    else:
        return(100)

if __name__ == "__main__":
    main()