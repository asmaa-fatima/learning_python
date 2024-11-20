from blackjack_logo import logo 
import random
import os


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(hand):
    score = sum(hand)
    while score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score    


def blackjack():

    dealer_cards = [random.choice(cards), random.choice(cards)]
    user_cards = [random.choice(cards), random.choice(cards)]

    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's first card: {dealer_cards[0]}")

    if sum(dealer_cards) == 21:
        print("Lose, opponent has Blackjack 😱")
    elif sum(user_cards) == 21:
        print("Win with a Blackjack 😎")

    while calculate_score(dealer_cards) < 17:
        new_card = random.choice(cards)
        dealer_cards.append(new_card)


    while calculate_score(user_cards) < 22:

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

    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score} \nComputer's final hand: {dealer_cards}, final score: {dealer_score}")

    if user_score > dealer_score:
        if user_score > 21:
            print("You went over. You lose 😭")
        else:
            print("You WIN 😃")
    elif dealer_score > user_score:
        if dealer_score > 21 :
            print("Opponent went over. You win 😁")            
        else:
            print("You lose 😤")
    else:
        print("DRAW 🙃")


def begin_blackjack():
    while input("Do you want to play a game of Blackjack? y/n: ").lower() == 'y':
        os.system("clear")
        print(logo)
        blackjack()

begin_blackjack()
