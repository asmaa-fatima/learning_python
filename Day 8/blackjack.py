from blackjack_logo import logo 
import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def blackjack():

    dealer_cards = [random.choice(cards), random.choice(cards)]
    user_cards = [random.choice(cards), random.choice(cards)]

    if sum(dealer_cards) == 21:
        print("Lose, opponent has Blackjack 😱")
    elif sum(user_cards) == 21:
        print("Win with a Blackjack 😎")

    while sum(dealer_cards) < 17:
        new_card = random.choice(cards)
        dealer_cards.append(new_card)

    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's first card: {dealer_cards[0]}")

    while True and sum(user_cards) < 22:

        card_pass = input("Type 'y' to get another card, type'n' to pass: ").lower()
        if card_pass == "y":
            new_card = random.choice(cards)
            user_cards.append(new_card)
            print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
            
        elif card_pass == 'n':
            print("Game Ended")
            break
        else:
            print("Invalid input Please type y/n.")

    print(f"Your final hand: {user_cards}, final score: {sum(user_cards)} \nComputer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")

    if sum(user_cards) > sum(dealer_cards):
        if sum(user_cards) > 21:
            print("You went over. You lose 😭")
        else:
            print("You WIN 😃")
    elif sum(dealer_cards) > sum(user_cards):
        if sum(dealer_cards) > 21 :
            print("Opponent went over. You win 😁")            
        else:
            print("You lose 😤")
    else:
        print("DRAW 🙃")

    begin_blackjack = input("Do you want to play a game of Blackjack? y/n: ").lower()

    if begin_blackjack == 'y':
        print(logo)
        blackjack()


begin_blackjack = input("Do you want to play a game of Blackjack? y/n: ").lower()

if begin_blackjack == 'y':
    print(logo)
    blackjack()



