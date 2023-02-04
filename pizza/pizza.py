import sys
import csv
from tabulate import tabulate

try:
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) == 2 and ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
except FileNotFoundError:
    sys.exit("File does not exist")

price = []

with open(f"{sys.argv[1]}") as file:
    reader = csv.reader(file)
    for row in reader:
        price.append(row)

print(tabulate(price[1:], headers=price[0], tablefmt="grid"))