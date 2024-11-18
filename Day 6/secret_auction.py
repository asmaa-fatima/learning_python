import secret_aution_logo
import os

print(secret_aution_logo.logo)

auction = {}
end_auction = False

while not end_auction:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    auction[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    os.system('clear')
    if other_bidders == "no" or other_bidders == "n":
        end_auction = True
    elif other_bidders == "yes" or other_bidders == "y":
        os.system('clear')


#using max
# highest_bidder = max(auction, key=auction.get)
# highest_bid = auction[highest_bidder]


highest_bid = 0
highest_bidder = ''

for bidder, bid in auction.items():
    if bid > highest_bid:
        highest_bid = bid
        highest_bidder = bidder

print(f"The winner is {highest_bidder} with a bid of {highest_bid}")



# print(auction)

