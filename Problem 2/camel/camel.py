def main ():
    string = input("camelCase: ")
    snake(string)

def snake(name):
    for letter in name:
        if letter.islower():
            print(letter, end ="")
        else:
            print(f"_{letter.lower()}", end ="")

main()
