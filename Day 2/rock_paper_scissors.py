import random

print("Welcome to Rock, Paper, Scissors!")
rock = "🪨 "
paper = '📜'
scissor = '✂️ '

game_images = [rock, paper, scissor]
print(game_images)

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(0, 2)

if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
elif user_choice == 0: 
  if computer_choice == 0:
    print("It's a draw!")
  elif computer_choice == 1:
    print(f"You lose! {paper} beats {rock}")
  else:
    print(f"You win! {rock} beats {scissor}")

elif user_choice == 1:
  if computer_choice == 0:
    print(f"You win! {paper} beats {rock}")
  elif computer_choice == 1:
    print("It's a draw!")
  else:
    print(f"You lose! {scissor} beats {paper}")

else:
 if computer_choice == 0:
    print(f"You lose! {rock} beats {scissor}")
 elif computer_choice == 1:
    print(f"You win! {scissor} beats {paper}")
 else:
    print("It's a draw!")

                  