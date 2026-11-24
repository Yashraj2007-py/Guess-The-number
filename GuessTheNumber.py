import random

secret = random.randint(1, 100) #random number between 1 and 100


attempts = 0
#initial commit
while True:
    guess = int(input("Guess a number between 1 to 100: "))
    if guess < secret:
        print("too low ")
    elif guess > secret:
        print("too high")
    elif guess == secret:
        print("congratulations! You guessed the number in", attempts, "attempts.")
        break
    attempts += 1

