import emoji

def main():
    msg = input_user()
    msg_emoji = convert_emoji(msg)

    print (msg_emoji)

def input_user():
    return input("Input: ")

def convert_emoji(msg):
   return emoji.emojize(msg)

main()
