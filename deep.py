ans = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
ans = ans.strip().casefold()
if ans in ["42","forty-two","forty two"]:
    print("Yes")
else:
    print("No")
