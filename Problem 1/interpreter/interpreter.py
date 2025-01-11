x, y, z = input("Expression: ").split(" ")
n = 2
match y:
    case "+":
        n = float(x)+float(z)
        print(f"{n}")
    case "-":
        n = float(x)-float(z)
        print(f"{n}")
    case "/":
        n = float(x)/float(z)
        print(f"{n}")
    case "*":
        n = float(x)*float(z)
        print(f"{n}")
