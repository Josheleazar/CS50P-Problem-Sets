import sys

def main():
    unts = input("Units: ").replace(",", "")
    estrent = input("Rent(USD): ").replace(",", "")
    unt, estrnt = assets(unts, estrent)
    revenue = annual_rev(unt, estrnt)
    try:
        price = int(input("Price(USD): ").replace(",", ""))
        mrktcp = cap_rate(revenue, price)
        print (f"Capitalization Rate: {mrktcp}%")
    except ValueError:
        sys.exit("Invalid Price")

def assets(unts, estrent):
    try:
        unt = int(unts)
        estrnt = int(estrent)
        return unt, estrnt
    except ValueError:
        sys.exit("Invalid Units and/or Rent Values")

def annual_rev(unt, estrnt):
    rev = unt*estrnt
    return rev

def cap_rate(rev, price):
    rev = rev*12
    cap = (rev/price)*100
    cap = round(cap, 1)
    return cap

if __name__ == "__main__":
    main()

