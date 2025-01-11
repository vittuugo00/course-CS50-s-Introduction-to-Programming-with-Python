def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    fuel = fraction.split(sep="/")
    x = int(fuel[0])
    y = int(fuel[1])

    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("X and/or Y must be integers.")
    if x > y:
        raise ValueError("X cannot be greater than Y.")
    if y == 0:
        raise ZeroDivisionError("Y cannot be zero.")

    percentage = (x/y) * 100
    return round(percentage)

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
    