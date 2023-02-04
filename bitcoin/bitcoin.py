import json
import requests
import sys

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    elif sys.argv[1].isalpha():
        sys.exit("Command-line argument is not a number")

    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    dict = r.json()
except requests.RequestException:
    sys.exit

usd = dict["bpi"]["USD"]["rate_float"]
amount = usd * float(sys.argv[1])
print(f"${amount:,.4f}")
