def main():
    items = {}
    while True:
        try:
            item = input().upper()
            if item in items:
                items[item] = items[item] + 1
            else:
                items[item] = 1
        except EOFError:
            alphatic_dict = dict(sorted(items.items()))

            for key, value in alphatic_dict.items():
                print(f"{value} {key}")
            break
        except Exception as e:
            print("An error occurred:", e)
main()
