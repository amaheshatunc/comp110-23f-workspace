"""Game that only completes when you guess the right number"""

from random import randint

secret: int = randint(1,10)
guess: int = int(input("Guess a number between 1 and 10: "))
number_of_tries: int = 3
tries_count: int = 0

while (guess != secret) and (tries_count < number_of_tries):
    print("Wrong!")
    if (guess < 1) or (guess > 10):
        print("This is not in between 1 and 10")
    if guess > secret:
        print("your guess was too high")
    else: 
        print("your guess was too low!")
    guess = int(input("Guess again: "))
    tries_count += 1
if guess == secret:
    print("Correct!")