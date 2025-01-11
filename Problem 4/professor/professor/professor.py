import random

def main():
    score = problems()
    print(f"Score: {score}")

def get_level():
    while True:
        lv = input("Level: ")
        if (lv.isnumeric()):
            if (lv == "1" or lv == "2" or lv == "3"):
                return int(lv)

def generate_integer(level):
    y = 0
    x = 0
    match level:
        case 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        case 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        case 3:
            x = random.randint(100, 999)
            y = random.randint(100, 999)
    return x, y

def problems():
    level = get_level()
    score = 0
    for _ in range(1, 10):
        tries = 0
        x, y = generate_integer(level)
        while tries < 3:
            answer = input(f"{x} + {y} = ")
            if (answer.isnumeric() and int(answer) == x + y):
                score = score + 1
                break
            else:
                if (tries < 3):
                    tries = tries + 1
                    print("EEE")
                    if (tries == 3):
                        print(f"{x} + {y} = {x+y}")
    return score

if __name__ == "__main__":
    main()
