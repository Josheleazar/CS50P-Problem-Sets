count = 1
listing = {}
while True:
    try:
        item = input().upper()
        if item in listing:
            listing[item] = listing[item] + 1
        else:
            listing[item] = 1
    except EOFError:
        for i in sorted(listing.keys()):
            print(listing[i], i)
        break


