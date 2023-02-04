def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    ans = gauge(percentage)
    print(f"{ans}")

def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            ans = int(x)/int(y)
            ans = ans * 100
            ans = round(ans)
            if 0 <= ans <= 100:
                return ans
        except (ValueError, ZeroDivisionError):
            pass

def gauge(percentage):
    if percentage <= 1 and percentage >= 0:
        return "E"
    elif percentage >= 99 and percentage <= 100:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()