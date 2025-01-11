def main():
    string = input("input: ")
    nwstrng = shorten(string) #without vowels
    print(f"Output: {nwstrng}")

def shorten(word):
    nwstrng = word
    for letter in word:
        if checkVowel(letter):
            nwstrng = nwstrng.replace(letter,"")

    return nwstrng

def checkVowel(letter):
    letter = letter.lower()
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        return True
    else:
        return False

if __name__ == "__main__":
    main()
