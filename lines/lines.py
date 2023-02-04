import sys
fname = sys.argv[1]

try:
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif fname[-3:] != ".py":
        sys.exit("Not a Python file")
    else:
        with open(f"{fname}", "r") as file:
            lst = file.readlines()
            count = 0
            for l in lst:
                if l.lstrip().startswith("#"):
                    continue
                elif l.isspace() or l == "\n":
                    continue
                else:
                    count = count + 1
except FileNotFoundError:
    sys.exit("File does not exist")

print(f"{count}")