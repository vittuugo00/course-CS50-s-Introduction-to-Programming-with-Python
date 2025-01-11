import random
import sys

def main():
    lv = getting_lv()
    number = random.randint(1, lv)
    guess_game(number)

def getting_lv():
    while True:
        lv = input("Level: ")
        if lv.isnumeric():
            return int(lv)
def getting_guess():
    while True:
        guess = input("Guess: ")
        if guess.isnumeric():
            return int(guess)

def guess_game(number):
    while True:
        guess = getting_guess()

        if guess > number:
            print("Too large!")
        elif guess < number:
            print("Too small!")
        elif guess == number:
            sys.exit("Just right!")
            
main()
