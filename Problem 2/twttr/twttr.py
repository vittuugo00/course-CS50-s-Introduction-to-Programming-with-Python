def main():
    string = input("input: ")
    nwstrng = voweless(string) #without vowels
    print(f"Output: {nwstrng}")

def voweless(s):
    nwstrng = s
    for c in s:
        if checkVowel(c):
            nwstrng = nwstrng.replace(c,"")

    return nwstrng

def checkVowel(letter):
    letter = letter.lower()
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        return True
    else:
        return False

main()
