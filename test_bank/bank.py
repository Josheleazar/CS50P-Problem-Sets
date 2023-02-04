def main():
    greeting = input("Greeting: ")
    grt = value(greeting)
    if grt == 0:
        print("$0")
    elif grt == 20:
        print("$20")
    else:
        print("$100")

def value(greeting):
    greeting = greeting.strip().casefold()
    if greeting[0:5] == "hello":
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
