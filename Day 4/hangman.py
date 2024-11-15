import random
import hangman_words
# import hangman_stages
from hangman_stages import stages

guessed_letters = []
player_lives = 6

chosen_word = random.choice(hangman_words.word_list)
display = ["_"] * len(chosen_word)

print("The chosen word is: " + chosen_word)
print(f"{' '.join(display)}")
print(stages[6])

display = ["_"] * len(chosen_word)

while "_" in display and player_lives > 0:

  guess = input("Guess a letter: ").lower()

  clear()

  if guess in guessed_letters:
    print(f"You already guessed {guess}. Try again.")
    print(f"{' '.join(display)}")
    print(stages[player_lives])
    continue

  guessed_letters.append(guess)

  if guess in chosen_word:
    for position in range(len(chosen_word)):
      letter = chosen_word[position]
      if "_" in display and letter == guess:
        display[position] = guess

  else:
    player_lives -= 1
    print(f"You guessed {guess}, that's not in the word. You lose a life.")

  print(f"{' '.join(display)}")
  print(stages[player_lives])

if '_' not in display:
  print("Congratulatios! You win")
else:
  print("You lose")
