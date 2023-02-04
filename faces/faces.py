def main():
    face = input()
    fac = convert(face)
    print(fac)

def convert(face):
    face = face.replace(":(", "🙁")
    face = face.replace(":)", "🙂")
    return f"{face}"


if __name__ == "__main__":
    main()