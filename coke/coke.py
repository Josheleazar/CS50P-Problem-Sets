due = 50
while due > 0:
    print("Amount Due: ", due)
    n = input("Insert Coin: ")
    while n not in["5","10","25"]:
        print("Amount Due: ", due)
        n = input("Insert Coin: ")
        break
    due = due - int(n)
    if due <= 0:
        print("Change Owed: ", int(due/-1))
        break
