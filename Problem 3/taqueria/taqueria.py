def main():
    menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

    try:
        order_total = 0
        while True:
            item = input("Item: ").title()
            if item in menu:
                order_total = menu[item] + order_total
                print(f"Total: ${'{:.2f}'.format(order_total)}")
    except EOFError:
        item = ""
        print("\n")
    except TypeError:
        print("There is an error with this dish, please select another one")

main()
