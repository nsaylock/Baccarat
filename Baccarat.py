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

    
    print("Welcome to Baccarat")
    print("Minimum bet is $60")
    print("Winning bets on Banker are subject to 5% commission")
    bankroll = int(input("How much money are you bringing to the table? $"))
    bet = 1

    # Start the while loop
    while bankroll > 0 and bet > 0:
        bankerHand = []
        playerHand = []
        bankerTotal = 0
        playerTotal = 0
        naturalStand = False
        playerThirdCard = 100

        betSide = "q"
        while betSide != "p" and betSide != "b":
            betSide = input("Choose Betting Side: Player or Banker (p/b): ")
            if betSide != "p" and betSide != "b":
                print("Invalid Input. Try Again")

        bet = int(input("Place Bet: $"))
        while bet < 60 or bet > bankroll:
            if bet < 60:
                print("Minimum bet is $60")
                bet = int(input("Try another amount: $"))
            elif bet > bankroll:
                bet = int(input("You don't have that much money. Try again: $"))
            elif bet != int:
                bet = int(input("Invalid input. Try again: $"))
    
        dealCard(deck, playerHand)
        dealCard(deck, bankerHand)
        dealCard(deck, playerHand)
        dealCard(deck, bankerHand)
        playerTotal = calculateTotal(playerHand)
        bankerTotal = calculateTotal(bankerHand)
        playerInitTotal = playerTotal

        displayTable(bankerHand, playerHand, bankerTotal, playerTotal, betSide, bet, bankroll)

        # Natural Stand
        if bankerTotal > 7 or playerTotal > 7:
            naturalStand = True

        # Player Decision tree
        if not(naturalStand):
            if playerTotal >= 0 and playerTotal < 6:
                dealCard(deck, playerHand)
                playerThirdCard = playerHand[2].value
                playerTotal = calculateTotal(playerHand)
                displayTable(bankerHand, playerHand, bankerTotal, playerTotal, betSide, bet, bankroll)
            

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
            displayTable(bankerHand, playerHand, bankerTotal, playerTotal, betSide, bet, bankroll)

        bankroll = compareHands(bankerTotal, playerTotal, betSide, bet, bankroll)

        print("\n")
    #^ End of While loop
    if bankroll == 0:
        print("You ran out of money, better luck next time")
    else:
        print("Player Quit")

#^ Main indent level
####################### END OF MAIN() ##############################

def compareHands(btotal, ptotal, betSide, bet, bankroll):
    if btotal == ptotal:
        print("Push")
        print("Bankroll: $",bankroll)
    elif btotal > ptotal:
        print("Banker Wins")
        print("Bankroll: $",bankroll,end="")
        if betSide == "b":
            bankroll += round(bet*0.95)
            print(" + $", round(bet*0.95))
        else:
            bankroll -= bet
            print(" - $", bet)
    elif btotal < ptotal:
        print("Player Wins")
        print("Bankroll: $",bankroll,end="")
        if betSide == "b":
            bankroll -= bet
            print(" - $", bet)
        else:
            bankroll += bet
            print(" + $", bet)
    return bankroll

def calculateTotal(hand):
    total = 0
    for card in hand:
        total += card.value
        if total >= 10:
            total -= 10
    if total == 10:
        total = 0
    return total
    

def displayTable(bhand, phand, btotal, ptotal, betSide, bet, bankroll):
    
    printBankerPlayerBoxes(betSide, bet)

                                                                        # Print Top Lines of cards
    for card in phand:
        for i in range(5):
            print("\u2582",end="")
        print("  ",end="")
    spaces(phand)
    for card in bhand:
        for i in range(5):
            print("\u2582",end="")
        print("  ",end="")
    print()

                                                             #Print 1st row of side lines
    for card in phand:
        print("\u258F   \u2595  ", end="")
    spaces(phand)
    for card in bhand:
        print("\u258F   \u2595  ", end="")
    print()
                                                                            #print 2nd row with card names inside
    for card in phand:
        print("\u258F",end="")
        printCard(card)
        if card.name[0:2] == "10":
            pass
        else:
            print(" ",end="")
        print("\u2595",end="  ")
    spaces(phand)
    for card in bhand:
        print("\u258F",end="")
        printCard(card)
        if card.name[0:2] == "10":
            pass
        else:
            print(" ",end="")
        print("\u2595",end="  ")
    print()
                                                                                #print 3rd row side lines (same as 1st)
    for card in phand:
        print("\u258F   \u2595  ", end="")
    spaces(phand)
    for card in bhand:
        print("\u258F   \u2595  ", end="")
    print()

                                                                                            #Print bottom lines
    for card in phand:
        for i in range(5):
            print("\u2594",end="")
        print("  ",end="")
    spaces(phand)
    for card in bhand:
        for i in range(5):
            print("\u2594",end="")
        print("  ",end="")
    print()
    
    print("\nTotal:",ptotal,"                     Total:",btotal)
    
                                                                                            # Display bankroll

    print("\nBankroll: $", bankroll)

    input("\n-----------------------------------------------------------")

def spaces(phand):   #Spaces between player ---> banker cards
    if len(phand) == 3:
        print("         ",end="")
    else:
        print("                ",end="")
    
def printBankerPlayerBoxes(betSide, bet):
    for i in range(50):
        if i > 19 and i < 30:
            print(" ",end="")
        else:
            print("\u2582", end="")
    
    print("")
    for i in range(5):
        if i == 2:
            print("\u258F      PLAYER       \u258F         ",end="")
            print("\u258F      BANKER       \u258F",end="")
            print("")
        elif i == 3:
            if betSide == "p":                                  # Display bet on player side
                print("\u258F      $",bet ,end="")
                for i in range(11 - len(str(bet))):
                    print(" ", end="")
                print("\u258F         ", end="")
                print("\u258F                   \u258F",end="")
            elif betSide == "b":                                    # Display bet on banker side
                print("\u258F                   \u258F         ",end="")
                print("\u258F      $",bet, end="")
                for i in range(11 - len(str(bet))):
                    print(" ", end="")
                print("\u258F",end="")
            print("")
        else:
            for i in range(51):
                if i == 0 or i == 20 or i == 30 or i == 50:
                    print("\u258F", end="")
                else:
                    print(" ",end="")
            print("")

    for i in range(50):
        if i > 19 and i < 30:
            print(" ",end="")
        else:
            print("\u2594", end="")
    print()

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
        print("\u2660", end="")
    elif card.name[lastChar] == "C":
        print("\u2663", end="")
    elif card.name[lastChar] == "H":
        print("\u2665", end="")
    else:
        print("\u2666", end="")




if __name__ == "__main__":
    main()