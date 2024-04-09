# Day 11 Capstone Project - BlackJack/21 Game

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

firstCards = [cards[random.randint(0,12)],cards[random.randint(0,12)]]
computerCards = [cards[random.randint(0,12)],cards[random.randint(0,12)]]

total =0

def myCardSum(cardList):
    global total
    for card in cardList:
        total=total+card
    return total    

def firstHit():
    print(f"Your Cards are: {firstCards}. Current Score: {myCardSum(firstCards)}")
    print(f"computer's first card: {computerCards[0]}")
    hitOrPass()

def nextHits():
    # global total
    print(f"Your Cards are: {firstCards}. Current Score: {total}")
    if total==21:
        print("You won")
        return
    if total>21:
        print("Your sum greater than 21. You lost")
        return
    


def hit():
    wish = input("Do you want to play a game of BlackJack? Type 'Y'or 'N'")
    if wish == 'Y':
        firstHit()

def hitOrPass():
    global total
    hitPass =input("Type 'Y' to get another card or 'N' to Pass")
    if hitPass == 'Y':
        firstCards.append(cards[random.randint(0,12)])
        total+=firstCards[len(firstCards)-1]
        nextHits()
    else:
        print(f"computer's second card: {computerCards[1]}")


firstHit()

