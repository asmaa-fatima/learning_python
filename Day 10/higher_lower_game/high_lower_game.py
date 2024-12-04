from high_lower_game_art import logo
from high_lower_game_art import vs
from highhigh_lower_game_data import data
import random
import os



score = 0


def start_game():
    global score
    user_a = random.choice(data)
    user_b = random.choice(data)

    while user_a == user_b: 
        user_b = random.choice(data)

    

    while True:

        print(logo)
        
        print(f"Compare A: {user_a["name"]}, a {user_a["description"]}, from {user_a["country"]}")
        print(vs)
        print(f"Against B: {user_b["name"]}, a {user_b["description"]}, from {user_b["country"]}")

        max_followers = max(user_a["follower_count"], user_b["follower_count"])

        player_answer = input("Who has many followers? Type 'A' or 'B': ").lower()

        if player_answer == "a":
            choosen_user = user_a
        elif player_answer =="b":
            choosen_user = user_b
        else:
            print("Invalid Input")

            continue
        

        if choosen_user["follower_count"] == max_followers:
            score +=1
            os.system('cls')
            print(f"You're right! Current score: {score}")
            user_a = user_b
            user_b = random.choice(data)
            while user_a == user_b: 
                user_b = random.choice(data)
        else:
            os.system('cls')
            print(f"Sorry, that's wrong. Final score: {score}")
            break


start_game()


