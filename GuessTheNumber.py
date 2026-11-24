import random


secret = random.randint(1, 100) #random number between 1 and 100
attempts = 0
max_attempts=7
while attempts < max_attempts:
    try:
        guess = int(input("guess a number between 1 and 100: "))
    except ValueError:
        print("please enter a number")
        continue
    attempts +=1

    if guess < secret:
        print("too low")
    elif guess > secret:
        print("too high")
    else:
        print("you guessed it in", attempts, "attempts")
        break

else:
    print("you lost! the number was", secret, ". Better luck next time. Try again")


