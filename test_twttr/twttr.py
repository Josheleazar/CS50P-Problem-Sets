def main():
    word = input("Input: ")
    letter = shorten(word)
    print(f"{letter}", end="")

def shorten(word):
    strng = ""
    for c in word:
        if c.lower() in ["a","e","i","o","u"]:
            pass
        else:
            strng = strng + c
    return strng

if __name__ == "__main__":
    main()