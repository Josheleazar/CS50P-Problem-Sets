import re
import sys


def main():
    time = input("Hours: ")
    try:
        print(convert(time))
    except ValueError:
        sys.exit("ValueError")


def convert(time):
    sim = re.search(
        r"^([1-9][0-2]?)(?:\:)?(0?[0-9]|[1-4][0-9]|5[0-9])? (AM|PM) ?(?:to) ?([1-9][0-2]?)(?:\:)?(0?[0-9]|[1-4][0-9]|5[0-9])? (AM|PM)$",
        time,
        re.IGNORECASE,
    )
    if sim:
        parts = sim.groups()
        H1 = int(parts[0])
        T1 = parts[2].lower()
        H2 = int(parts[3])
        T2 = parts[5].lower()
        if H1 > 12:
            raise ValueError
        if H2 > 12:
            raise ValueError
        if T1 == "pm" and H1 != 12:
            H1 = H1 + 12
        if T2 == "pm" and H2 != 12:
            H2 = H2 + 12
        if T1 == "am" and H1 == 12:
            H1 = H1 - 12
        if T2 == "am" and H2 == 12:
            H2 = H2 - 12
        M1 = parts[1]
        M2 = parts[4]
        if M1 == None:
            M1 = 0
        elif int(M1) >= 60:
            raise ValueError
        else:
            M1 = int(M1)
        if M2 == None:
            M2 = 0
        elif int(M2) >= 60:
            raise ValueError
        else:
            M2 = int(M2)
        T4H = f"{H1:02}:{M1:02} to {H2:02}:{M2:02}"
        return T4H
    else:
        raise ValueError


if __name__ == "__main__":
    main()
