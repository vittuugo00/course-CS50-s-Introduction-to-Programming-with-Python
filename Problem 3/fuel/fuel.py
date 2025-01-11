def main():
    while True:
        try:
            fraction = input("Fraction: ").split(sep="/")
            print(get_fuel(fraction))
            break
        except (ValueError, ZeroDivisionError):
            pass

def get_fuel(f):
    fuel = (int(f[0]) / int(f[1])) * 100
    if fuel < 95 and fuel > 5:
        return f"{int(fuel)}%"
    elif fuel >= 95:
        return "F"
    elif fuel <= 5:
        return "E"

main()
