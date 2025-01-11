def main():
    fruits = [
        {"name": "apple", "calories": "130"},
        {"name": "avocado", "calories": "50"},
        {"name": "sweet cherries", "calories": "100"},
        {"name": "banana", "calories": "110"},
        {"name": "cantaloupe", "calories": "50"},
        {"name": "kiwifruit", "calories": "90"},
        {"name": "pear", "calories": "100"}
    ]
    item = input("Item: ")
    nutrition(fruits, item)

def nutrition(fruits, item):
    for fruit in fruits:
        if item.casefold() == fruit["name"].casefold():
            print("Calories: ", end = "")
            print(fruit["calories"])

main()
