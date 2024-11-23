import random
from number_guessing_game_logo import logo


actual_number =  random.randint(0, 100)

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

while True:
    diffculty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if diffculty == 'easy':
        attempts_left = 10
        break
    elif diffculty == 'hard':
        attempts_left = 5
        break
    else:
        print("Invalid Answer. Select again!")

print(f"You have {attempts_left} attempts remaining to guess the number.")

while attempts_left > 0:
    guessed_Number = int(input("Make a guess: "))

    if guessed_Number > actual_number :
        print("Too high.\nGuess Again")
        attempts_left -= 1
    elif guessed_Number < actual_number:
        print("Too low.\nGuess Again")
        attempts_left -= 1
    elif guessed_Number == actual_number:
        print(f"You got it! The answer was {actual_number}")
        break
    else:
        print("Invalid Input. Try Again")
    
    print(f"You have {attempts_left} attempts remaining to guess the number.")
    
