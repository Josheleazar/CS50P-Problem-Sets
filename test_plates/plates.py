def main():
    s = input("Plate: ")
    if is_valid(s):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if alphabet(s):
        return False
    elif char(s):
        return False
    elif digit0(s):
        return False
    elif midletter(s):
        return False
    elif abno(s):
        return False
    else:
        return True

def alphabet(s):
    for c in s:
        if s[0:1].isnumeric():
            return True

def char(s):
    if len(s) > 6 or len(s) < 2:
        return True

def digit0(s):
    for c in s:
        if c.isdigit() and c == "0":
            return True
        elif c in ["1","2","3","4","5","6","7","8","9",]:
            break

def midletter(s):
    for index, c in enumerate(s[:-1]):
        if c.isdigit() and s[index + 1].isalpha():
            return True

def abno(s):
    c = s[0:len(s)]
    p = ["!","@","#","$","%","&","?","."]
    for c in s:
        if c in p:
            return True
            
if __name__ == "__main__":
    main()
