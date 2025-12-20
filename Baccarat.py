"""
    Filename: Baccarat.py
    Developer: Nick Saylock
    Date: 2025-12-20
    Version 1.0
    Description: Baccarat
"""
import random


class Card:
    pass

# --------------------- START MAIN() -------------------------------
def main():
    deck = []
    initializeDeck(deck)
    for i, card in enumerate(deck):     #Displays the deck for testing purposes
        printCard(card)
        if (i + 1) % 13 == 0:
            print("")
    print("")
                        # Round Start

    playerHand = []
    bankerHand = []

    dealCard(deck, playerHand)
    dealCard(deck, bankerHand)
    dealCard(deck, playerHand)
    dealCard(deck, bankerHand)

    print("BANKER               PLAYER")
    printCard(bankerHand[0])
    printCard(bankerHand[1])
    print("             ",end="")
    printCard(playerHand[0])
    printCard(playerHand[1])
    print("             ")

    for i in range(59):
        dealCard(deck, playerHand)
        printCard(playerHand[i])

    print("\n")
    for i, card in enumerate(deck):     #Displays the deck for testing purposes
        printCard(card)
        if (i + 1) % 13 == 0:
            print("")
    print("\n",end="\n")
                  

####################### END OF MAIN() ##############################

def dealCard(deck, hand):
    if len(deck) == 0:
        initializeDeck(deck)
    hand.append(deck[0])
    deck.remove(deck[0])
    

def initializeDeck(deck):
    faces = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    suits = ["S","C","H","D"]
    for face in faces:
        for suit in suits:
            card = Card()
            card.name = face + suit
            if face == "J" or face == "Q" or face == "K":
                card.value = 10
            elif face == "A":
                card.value = 11
            else:
                card.value = int(face)
            deck.append(card)

    random.shuffle(deck)

def printCard(card):
    lastChar = len(card.name) - 1
    if len(card.name) == 2:
        print(card.name[0], end="")
    elif len(card.name) == 3:
        print(card.name[0:1], end="")

    if card.name[lastChar] == "S":
        print("\u2660", end="")
    elif card.name[lastChar] == "C":
        print("\u2663", end="")
    elif card.name[lastChar] == "H":
        print("\u2665", end="")
    else:
        print("\u2666", end="")

    print(" ", end="")



if __name__ == "__main__":
    main()