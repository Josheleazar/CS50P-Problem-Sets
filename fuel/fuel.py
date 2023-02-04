while True:
    try:
        while True:
            s = input("Fraction: ")
            x, y = s.split("/")
            ans = int(x)/int(y)
            ans = ans * 100
            ans = round(ans)
            if 0 <= ans <= 100:
                break
        if ans <= 1 :
            print("E")
        elif ans >= 99 and ans <= 100:
            print("F")
        else:
            print(f"{ans}%")
        break
    except (ValueError, ZeroDivisionError):
        pass