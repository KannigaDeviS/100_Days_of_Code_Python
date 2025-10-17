import art
import random
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return 10
    else:
        return 5
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(0,100)
attempts = set_difficulty()
guessed = False
while attempts != 0:
    print(f"You have {attempts} remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it! The answer was {number}")
        guessed = True
        break
    elif guess > number:
        print("Too high.")
        attempts-= 1
    else:
        print("Too low.")
        attempts -= 1

if guessed == False:
    print("You've run out of guesses. Rerun the project")