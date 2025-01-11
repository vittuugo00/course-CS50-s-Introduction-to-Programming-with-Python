import inflect

p = inflect.engine()

def main():
    name_list = []
    while True:
        try:
            name = input("Name: ")
            name_list.append(name)

        except EOFError:
            if len(name_list) > 1:
                names = p.join(name_list)
                print(f"Adieu, adieu, to {names}")
            else:
                print(f"Adieu, adieu, to {name}")
            break
main()
