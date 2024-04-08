# Day 11 Capstone Project - BlackJack/21 Game

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

firstCards = [cards[random.randint(0,12)],cards[random.randint(0,12)]]
computerCards = [cards[random.randint(0,12)],cards[random.randint(0,12)]]

def myCardSum(cardList):
    sum =0
    for card in cardList:
        sum=sum+card

def firstHit():
    print(f"Your Cards are: {firstCards}. Current Score: {myCardSum(firstCards)}")
    print(f"computer's first card{computerCards[0]}")

def hit():
    wish = input("Do you want to play a game of BlackJack? Type 'Y'or 'N'")
    if wish == 'Y':
        firstHit()

hitOrPass = input("Type 'Y' to get another card or 'N' to Pass")
if hitOrPass == 'Y':
    firstCards.append(cards[random.randint(0,12)])
    firstHit()

firstHit()

