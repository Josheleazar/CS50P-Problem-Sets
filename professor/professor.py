import random


def main():
    level = get_level()
    result = run_through(level)
    print(f"Score:", result)

def run_through(level):
    trial = 0
    prblm = 0
    Score = 10
    while True:
        prblm = prblm + 1
        X = generate_integer(level)
        Y = generate_integer(level)
        sol = X + Y
        while True:
            try:
                ans = input(f"{X} + {Y} = ")
                ans = int(ans)
                if ans != sol and prblm < 10 and trial < 2:
                    print("EEE")
                    trial = trial + 1
                    Score = Score - 1
                elif trial == 2:
                    print(f"{X} + {Y} = ", sol, sep="" )
                    trial = 0
                    break
                else:
                    break
            except ValueError:
                print("EEE")
                continue
        if prblm == 10:
            return Score

def get_level():
    while True:
        try:
            n = input("Level: ")
            n = int(n)
            if n in [1,2,3]:
                return n
        except ValueError:
            pass

def generate_integer(level):
        if level == 1:
            nni = random.randint(0, 9)
            return nni
        elif level == 2:
            nni = random.randint(10, 99)
            return nni
        elif level == 3:
            nni = random.randint(100, 999)
            return nni
        else:
            raise ValueError


if __name__ == "__main__":
    main()