# concept learnr - dictionaries

# dictionary = {"first":1,
#            "second":2,
#            "third":3}

# print(dictionary.get("first"))


# Day 9 Project - Silent Auction

import os

def clear_terminal():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Unix/Linux/MacOS
    else:
        _ = os.system('clear')

print("Welcome to the Silent Auction Program")

def bidding():
    name = input("What's your name?")
    amount = int(input("Enter the amount: ₹"))
    bids ={name : amount}
    bidder=""
    highestBid = 0
    wish = input("Is there any other bidder? press 'Y' or 'N'\n")
    if wish=='Y':
        clear_terminal()
        bidding()
    else:
        for bid in bids:
            if bids[bid] > highestBid:
                highestBid = bids[bid]
                bidder=bid

        print(f"Highest Bid is {highestBid} By {bidder}")
        return
        
bidding()
