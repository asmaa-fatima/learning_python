from blackjack_logo import logo 
import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def blackjack():

    dealer_cards = [random.choice(cards), random.choice(cards)]
    user_cards = [random.choice(cards), random.choice(cards)]

    if sum(dealer_cards) == 21:
        

    while True and (sum(user_cards) < 22 or sum(dealer_cards) < 22):

        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Computer's first card: {dealer_cards[0]}")

        card_pass = input("Type 'y' to get another card, type'n' to pass:").lower()
        if card_pass == "y":
            new_card = random.sample(cards)
            user_cards.append(new_card)
            new_card = random.sample(cards)
        elif card_pass == 'n':
            print("Game Ended")
            break
        else:
            print("Invalid input Please type y/n.")

    if sum(user_cards) > sum(dealer_cards):
        if sum(user_cards) > 21:
            print("You went over. You lose 😭")
        elif sum(user_cards) == 21:
            print("You win, You have Bkackjack")
        else:
            print("You WIN 😃")
    elif sum(dealer_cards) > sum(user_cards):
        if sum(dealer_cards) > 21 :
            print("Opponent went over. You win 😁")
        elif sum(dealer_cards == 21):
            print("Lose, opponent has Blackjack 😱")
        else:
            print("You lose 😤")
    else:
        print("DRAW 🙃")


begin_blackjack = input("Do you want to play a game of Blackjack? y/n: ").lower()

if begin_blackjack == 'y':
    print(logo)
    blackjack()



