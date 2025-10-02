import random

random_number = random.randint(1, 3)
status = False

while not status:
    user_number = int(input("Guess a number between 1 and 3: "))
    if user_number != random_number:
        print("Try again!")
    else:
        print("You guessed it!")
        status = True