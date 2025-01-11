def main():
    coke()
    print("Change Owed: 0")

def coke(amount = 50):
    while amount != 0:
        print(f"Amount Due: {amount}")
        coin = input("Insert Coin: ")
        if(checkCoin(int(coin))):
            amount = (amount - int(coin))

def checkCoin(coin):
    if coin == 50 or coin == 25 or coin == 10 or coin == 5:
       return True
    else:
        return False

main()
