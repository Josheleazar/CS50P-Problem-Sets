import random
while True:
    try:
        n = input("Level: ")
        if int(n) > 0 and n.isnumeric():
            break
    except ValueError:
        pass

ans = random.randint(1, int(n))

while True:
    try:
        guess = input("Guess: ")
        guess = int(guess)
        if guess < ans:
            print("Too small!")
        elif guess > ans:
            print("Too large!")
        elif guess == ans:
            print("Just right!")
            break
    except ValueError:
        pass
