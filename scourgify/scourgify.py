import sys
import csv

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

namelist = []
try:
    with open(f"{sys.argv[1]}") as file:
        reader = csv.DictReader(file)
        for row in reader:
            l, f = row["name"].split(",")
            f = f.strip()
            namelist.append({"first": f,"last": l,"house": row["house"]})
        with open(f"{sys.argv[2]}", "w") as file2:
            fieldname = ['first', 'last', 'house']
            writer = csv.DictWriter(file2, fieldnames=fieldname)
            writer.writeheader()
            for nme in namelist:
                writer.writerow({"first": nme["first"],"last": nme["last"],"house":nme["house"]})

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")