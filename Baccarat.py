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
  
                        # Round Start

    bankerHand = []
    playerHand = []
    bankerTotal = 0
    playerTotal = 0
    naturalStand = False
    playerThirdCard = 100
    
    dealCard(deck, playerHand)
    dealCard(deck, bankerHand)
    dealCard(deck, playerHand)
    dealCard(deck, bankerHand)
    playerTotal = calculateTotal(playerHand)
    bankerTotal = calculateTotal(bankerHand)
    playerInitTotal = playerTotal

    displayTable(bankerHand, playerHand, bankerTotal, playerTotal)
    input("Press Enter to Continue")

    # Natural Stand
    if bankerTotal > 7 or playerTotal > 7:
        naturalStand = True

    # Player Decision tree
    if not(naturalStand):
        if playerTotal >= 0 and playerTotal < 6:
            dealCard(deck, playerHand)
            playerThirdCard = playerHand[2].value
            playerTotal = calculateTotal(playerHand)
            displayTable(bankerHand, playerHand, bankerTotal, playerTotal)
            input("Press Enter to Continue")

    # Banker decision tree
    if not(naturalStand):
        if playerThirdCard != 100:
            if bankerTotal >= 0 and bankerTotal < 3:
                dealCard(deck, bankerHand)
                bankerTotal = calculateTotal(bankerHand)
            elif bankerTotal == 3 and playerThirdCard != 8:
                dealCard(deck, bankerHand)
                bankerTotal = calculateTotal(bankerHand)
            elif bankerTotal == 4 and (playerThirdCard < 8):
                dealCard(deck, bankerHand)
                bankerTotal = calculateTotal(bankerHand)
            elif bankerTotal == 5 and (playerThirdCard > 3 and playerThirdCard < 8):
                dealCard(deck, bankerHand)
                bankerTotal = calculateTotal(bankerHand)
            elif bankerTotal == 6 and (playerThirdCard > 5 and playerThirdCard < 8):
                dealCard(deck, bankerHand)
                bankerTotal = calculateTotal(bankerHand)
        else:
            if bankerTotal >= 0 and bankerTotal < 6:
                dealCard(deck, bankerHand)
                bankerTotal = calculateTotal(bankerHand)
        displayTable(bankerHand, playerHand, bankerTotal, playerTotal)
        input("Press Enter to Continue")

    compareHands(bankerTotal, playerTotal)




    print("\n")

#^ Main indent level
####################### END OF MAIN() ##############################

def compareHands(btotal, ptotal):
    if btotal == ptotal:
        print("Push")
    elif btotal > ptotal:
        print("Banker Wins")
    elif btotal < ptotal:
        print("Player Wins")

def calculateTotal(hand):
    total = 0
    for card in hand:
        total += card.value
        if total >= 10:
            total -= 10
    if total == 10:
        total = 0
    return total
    

def displayTable(bhand, phand, btotal, ptotal):
    print("PLAYER               BANKER")
    cardSpaces = 1
    for card in phand:
        printCard(card)
        cardSpaces += len(card.name)
    if len(phand) == 3:
        cardSpaces += 1
    for i in range(20 - cardSpaces):
        print(" ",end="")
    for card in bhand:
        printCard(card)
    print("\nTotal:",ptotal,"            Total:",btotal)

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
    if lastChar == 1:
        print(card.name[0], end="")
    elif lastChar == 2:
        print(card.name[0:2], end="")

    if card.name[lastChar] == "S":
        print("\u2660", end=" ")
    elif card.name[lastChar] == "C":
        print("\u2663", end=" ")
    elif card.name[lastChar] == "H":
        print("\u2665", end=" ")
    else:
        print("\u2666", end=" ")




if __name__ == "__main__":
    main()