import emoji

char = input("Input: ")
d = []
d = char.split()
for ch in d:
    print(emoji.emojize(ch, language="alias"))
