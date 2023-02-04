from datetime import date, datetime
import sys
import inflect
p = inflect.engine()
import math





def main():
    bd = input("Date of Birth: ")
    birth = get_birthday(bd)
    ans = get_today() - birth
    print(f"{get_minutes(ans)} minutes")

def get_minutes(ans):
    seconds = ans.total_seconds()
    minute = int(seconds)/60
    minute = math.trunc(minute)
    minutes = p.number_to_words(minute, andword="")
    minutes = minutes.capitalize()
    return minutes

def get_today():
    today = date.today()
    return today

def get_birthday(bd):
    try:
        bday = datetime.strptime(bd, "%Y-%m-%d").date()
        return bday
    except ValueError:
        sys.exit(1)


if __name__ == "__main__":
    main()