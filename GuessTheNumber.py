import random

print("wellcome to the game ")
dificulty_level = int(input("\n please select difficulty level (1,2,3,4)"))


def maingame(max_range,max_attempts):
    secret = random.randint(1, max_range)  # random number between 1 and max_range
    attempts = 0
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"guess a number between 1 and {max_range}: "))
        except ValueError:
            print("please enter a number")
            continue
        attempts += 1

        if guess < secret:
            print("too low")
        elif guess > secret:
            print("too high")
        else:
            print("you guessed it in", attempts, "attempts")
            break

    else:
        print("you lost! the number was", secret, ". Better luck next time. Try again")

if dificulty_level ==1:
    maingame(10,3)
elif dificulty_level ==2:
    maingame(100,7)
elif dificulty_level ==3:
    maingame(1000,15)
elif dificulty_level ==4:
    maingame(10000,20)