import cowsay

def main():
    while True:
        who_say = choosing_who()
        print(" ") # just to make a blank line
        saying(who_say)
        print(" ") # just to make a blank line
        print(" ") # just to make a blank line
def choosing_who():
    for who in cowsay.char_names:
        if who != "tux":
            print(who, end = ", ")
        else:   
            print (who)
    try:
        while True:
            who = input("Please, choose one of the above who you want to talk: ").lower().lstrip()
            if who in cowsay.char_names:
                return who
            else:
                print("WRITE IT CORRECTLY PLEASE!")
    except:
        print("Something goes wrong, probably it is your fault!")

def saying(who_say):
    try:
        msg = input("Ok, you are a good user, now please, type a cool message: ")
        match who_say:
            case "beavis":
                cowsay.beavis(msg)
            case "cheese":
                cowsay.cheese(msg)
            case "cow":
                cowsay.cow(msg)
            case "daemon":
                cowsay.daemon(msg)
            case "dragon":
                cowsay.dragon(msg)
            case "fox":
                cowsay.fox(msg)
            case "ghostbusters":
                cowsay.ghostbusters(msg)
            case "kitty":
                cowsay.kitty(msg)
            case "meow":
                cowsay.meow(msg)
            case "miki":
                cowsay.miki(msg)
            case "milk":
                cowsay.milk(msg)
            case "pig":
                cowsay.pig(msg)
            case "stegosaurus":
                cowsay.stegosaurus(msg)
            case "stimpy":
                cowsay.stimpy(msg)
            case "trex":
                cowsay.trex(msg)
            case "turkey":
                cowsay.turkey(msg)
            case "turtle":
                cowsay.turtle(msg)
            case "tux":
                cowsay.tux(msg)
    except:
        print("Something goes wrong, it is probably yout fault!")
main()
