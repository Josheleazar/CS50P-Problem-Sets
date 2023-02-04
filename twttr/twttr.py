s = input("Input: ")
for c in s:
    if c.lower() in ["a","e","i","o","u"]:
        print("", end="")
    else:
        print(c, end="")
