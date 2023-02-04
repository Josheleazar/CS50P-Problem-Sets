months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    form = input("Date: ").strip()
    try:
        if form[0] in ["1","2","3","4","5","6","7","8","9"]:
            mm, dd, yyyy = form.split("/")
            if int(dd) < 32 and int(mm) < 13:
                mo = mm
                break
        elif form[0].isalpha() and "," in form:
                mm, dd, yyyy = form.split()
                dd = dd.replace(",","")
                for month in range(len(months)):
                    if mm == months[month]:
                        mo = month + 1
                if int(dd) < 32 and month < 13:
                    break

    except:
        print()
        pass

print(f"{int(yyyy)}-{int(mo):02d}-{int(dd):02d}")

