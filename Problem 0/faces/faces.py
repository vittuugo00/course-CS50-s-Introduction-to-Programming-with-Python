def convertEmoji(str):
    #happy emoji
    emoji = str.replace("(:","🙂")
    emoji = emoji.replace(":)","🙂")
    #sad emoji
    emoji = emoji.replace("):","🙁")
    emoji = emoji.replace(":(","🙁")

    print(emoji)


string = input()
convertEmoji(string)
