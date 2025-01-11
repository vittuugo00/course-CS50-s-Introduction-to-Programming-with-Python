str = input("Greeting: ").lower().strip()

if (str.find("hello", 0, 5) != -1):
    print("$0")
elif (str.find("h", 0, 1) != -1):
    print("$20")
else: print("$100")
