def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if s_lenght(s) and isletter(s) and valid_numeric(s) and valid_characs(s):
        return True
    else:
        return False

def s_lenght(s):
    if len(s) <= 6 and len(s) >= 2:
        return True
    else:
        return False

def isletter(s):
    aux = 0
    for c in s:
        aux = aux + 1
        if c.isnumeric() and aux <= 2:
            return False
        elif aux < 2:
            return True

def valid_numeric(s):
    aux = 0
    for c in s:
        if c.isnumeric():
            if c == "0" and aux == 0:
                return False
            aux = aux + 1
        elif aux >= 1:
            return False
    return True

def valid_characs(s):
    if s.isalnum():
        return True
    else:
        return False

if __name__ == "__main__":
    main()
