"""
    Filename: Baccarat.py
    Developer: Nick Saylock
    Date: 2025-12-20
    Version 1.0
    Description: Baccarat
"""
import random
import matplotlib.pyplot as plt
import numpy as np

class Card:
    pass

# --------------------- START MAIN() -------------------------------
def main():
    print("Welcome to Baccarat Simulation")
    print("Winning bets on Banker are subject to 5% commission\n")
    print("------------- Parameters ----------------")
    numOfDecks = int(input("Number of decks: "))
    bet = int(input("Bet Amount: $"))
    interval = int(input("Interval of Study: "))
    iterations = 25
    betSide = input("Choose betting side: Player, Banker, or Random (p/b/r): ")
    betRandom = "q"
    while betSide != "p" and betSide != "b" and betSide != "r":
            betSide = input("Choose Betting Side: Player or Banker or Random (p/b/r): ")
            if betSide != "p" and betSide != "b" and betSide != "r":
                print("Invalid Input. Try Again")
    if betSide == "r":
        betRandom = "r"
    repeat = "y"
    finalBankroll = []
    positiveOutcome = 0
    negativeOutcome = 0

    for j in range(interval*4):
        gamesWon = 0
        gamesLost = 0
        push = 0
        bankerWon = 0
        playerWon = 0
        bankroll = 0
        
        plotBankroll = [0]
        deck = []
        initializeDeck(deck, numOfDecks)
        # displayInitialDeck()
        
      
        for game in range(iterations):
            bankerHand = []
            playerHand = []
            bankerTotal = 0
            playerTotal = 0
            naturalStand = False
            playerThirdCard = 100
            if betRandom == "r":
                selector = random.randint(0, 1) #Could probable edit these numbers to change odds of bet side for ex. 25% player 75% banker
                if selector == 0:                  #might be (0, 3) where 0 = p and 1, 2, 3 = b
                    betSide = "p"
                else:
                    betSide = "b"

            dealCard(deck, playerHand, numOfDecks)
            dealCard(deck, bankerHand, numOfDecks)
            dealCard(deck, playerHand, numOfDecks)
            dealCard(deck, bankerHand, numOfDecks)
            playerTotal = calculateTotal(playerHand)
            bankerTotal = calculateTotal(bankerHand)

            # Natural Stand
            if bankerTotal > 7 or playerTotal > 7:
                naturalStand = True

            # Player Decision tree
            if not(naturalStand):
                if playerTotal >= 0 and playerTotal < 6:
                    dealCard(deck, playerHand, numOfDecks)
                    playerThirdCard = playerHand[2].value
                    playerTotal = calculateTotal(playerHand)
            

            # Banker decision tree
            if not(naturalStand):
                if playerThirdCard != 100:
                    if bankerTotal >= 0 and bankerTotal < 3:
                        dealCard(deck, bankerHand, numOfDecks)
                        bankerTotal = calculateTotal(bankerHand)
                    elif bankerTotal == 3 and playerThirdCard != 8:
                        dealCard(deck, bankerHand, numOfDecks)
                        bankerTotal = calculateTotal(bankerHand)
                    elif bankerTotal == 4 and (playerThirdCard < 8):
                        dealCard(deck, bankerHand, numOfDecks)
                        bankerTotal = calculateTotal(bankerHand)
                    elif bankerTotal == 5 and (playerThirdCard > 3 and playerThirdCard < 8):
                        dealCard(deck, bankerHand, numOfDecks)
                        bankerTotal = calculateTotal(bankerHand)
                    elif bankerTotal == 6 and (playerThirdCard > 5 and playerThirdCard < 8):
                        dealCard(deck, bankerHand, numOfDecks)
                        bankerTotal = calculateTotal(bankerHand)
                else:
                    if bankerTotal >= 0 and bankerTotal < 6:
                        dealCard(deck, bankerHand, numOfDecks)
                        bankerTotal = calculateTotal(bankerHand)

            bankroll = compareHands(bankerTotal, playerTotal, betSide, bet, bankroll)
            plotBankroll.append(bankroll)
            
            if bankerTotal > playerTotal:
                bankerWon += 1
                if betSide == "b":
                    gamesWon += 1
                else:
                    gamesLost += 1
            elif bankerTotal < playerTotal:
                playerWon += 1
                if betSide == "b":
                    gamesLost += 1
                else:
                    gamesWon += 1
            else:
                push += 1
                

        #^ End of for iterations loop
        if bankroll > 0:
            positiveOutcome += 1
        elif bankroll < 0:
            negativeOutcome += 1

        if j+1 == interval:
            data25 = [positiveOutcome, negativeOutcome]
            iterations *= 10
            positiveOutcome = 0
            negativeOutcome = 0
        elif j+1 == interval*2:
            data125 = [positiveOutcome, negativeOutcome]
            iterations *= 10
            positiveOutcome = 0
            negativeOutcome = 0
        elif j+1 == interval*3:
            data225 = [positiveOutcome, negativeOutcome]
            iterations *= 10
            positiveOutcome = 0
            negativeOutcome = 0
        elif j+1 == interval*4:
            data325 = [positiveOutcome, negativeOutcome]
            iterations *= 2
            positiveOutcome = 0
            negativeOutcome = 0
       
        print("----------- OUTCOMES -------------------")
        print("Simulated", iterations, "games of Baccarat")
        print("Final BankRoll: $", bankroll)
        print("Games Won: ", gamesWon)
        print("Games Lost: ", gamesLost)
        print("Banker Odds %", bankerWon/(iterations-push)*100)
        print("Player Odds %", playerWon/(iterations-push)*100)
        #repeat = input("Repeat? ")
        #if repeat != "y":
        #    break
        if betRandom == "r":
            betSide = "r"
        print("------------- Parameters ----------------")
        print("Number of decks: ", numOfDecks)
        print("Bet Amount: $", bet)
        print("Number of Iterations: ", iterations)
        print("Betting side:", betSide)

    outcomes = {
        'Positive': (data25[0], data125[0], data225[0], data325[0]),
        'Negative': (data25[1], data125[1], data225[1], data325[1])
    }

    x = np.arange(4)
    width = 0.25
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    for group, outcome in outcomes.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, outcome, width, label=group)
        ax.bar_label(rects, padding=3)
        multiplier += 1

    ax.set_title("Baccarat: Wins vs. Losses for # Hands Played")
    ax.set_ylabel("Outcomes of x hands played")
    ax.set_xlabel("# of Hands Played per Inteval")
    ax.set_xticks(x + width, ["25", '250', '2500', '5000'])
    ax.legend(loc='upper left', ncols=2)

    plt.show()

#^ Main indent level
####################### END OF MAIN() ##############################

def compareHands(btotal, ptotal, betSide, bet, bankroll):
    if btotal > ptotal:
        if betSide == "b":
            bankroll += round(bet*0.95)
        else:
            bankroll -= bet
    elif btotal < ptotal:
        if betSide == "b":
            bankroll -= bet
        else:
            bankroll += bet
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

def dealCard(deck, hand, numOfDecks):
    if len(deck) == 0:
        initializeDeck(deck, numOfDecks)
    hand.append(deck[0])
    deck.remove(deck[0])
    

def initializeDeck(deck, numOfDecks):
    for i in range(numOfDecks):
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

def displayInitialDeck():
    print("\nInitial Deck")
    print("1|", end="")
    d = 1
    for i, card in enumerate(deck):
        printCard(card)
        if (i + 1) % 13 == 0:
            print()
        if (i + 1) % 52 == 0:
            d += 1
            print()
            if d <= numOfDecks:
                print(d,"|",end="")
    print("\n")

if __name__ == "__main__":
    main()