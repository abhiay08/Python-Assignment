'''MINI PROJECT : 2
PROBLEM STATEMENT
Implement BlackJack using python.
- The game is required to be only player vs dealer
- Skip the implementation of ‘split’ and ‘doubling’.
Here is a list of some basic rules (except splitting and doubling):
The goal of blackjack is to beat the dealer's hand without going over 21.
Face cards are worth 10. Aces are worth 1 or 11, whichever makes a better hand.
Each player starts with two cards, one of the dealer's cards is hidden until the end.
To 'Hit' is to ask for another card. To 'Stand' is to hold your total and end your turn.
If you go over 21 you bust, and the dealer wins regardless of the dealer's hand.
If you are dealt 21 from the start (Ace & 10), you got a blackjack (instant win).
Blackjack usually means you win 1.5 the amount of your bet. Depends on the casino.
Dealer will hit until his/her cards total 17 or higher i.e once the player chooses to hold (and they aren't busted yet)
the dealer has to open the hidden card and keep hitting until the sum is 17 or more
If dealer gets busted, player wins
It is advised to play some games online/ read more about it before implementing.
Create a login system for the game as well:
A player can sign up:
- Ask for username and password
- Create a player table and save player details in MySQL database (password should be encrypted)
- usernames should be unique
Next, a player can log in to the system and start playing.
For every game store player’s final score, dealer’s final score, the result of the game (win or loss) and the
 timestamp  in a “results” table.
The player is greeted with a welcome menu on logging in, where they can select to view their scores:
A table that shows win/loss , scores of both dealer and player and date and time in DD/MM/YYYY HH:mm:ss format
The player is asked if they want to play more after each match
END OF MINI PROJECT PROBLEM STATEMENT
Submission status
'''

import os
import random

decks = input("Enter number of decks to use: ")

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * (int(decks) * 4)

wins = 0
losses = 0


def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11: card = "J"
        if card == 12: card = "Q"
        if card == 13: card = "K"
        if card == 14: card = "A"
        hand.append(card)
    return hand


def play_again():
    again = input("Do you want to play again? (Y/N) : ").lower()
    if again == "y":
        dealer_hand = []
        player_hand = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
        game()
    else:
        print("Bye!")
        exit()


def total(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total += 10
        elif card == "A":
            if total >= 11:
                total += 1
            else:
                total += 11
        else:
            total += card
    return total


def hit(hand):
    card = deck.pop()
    if card == 11: card = "J"
    if card == 12: card = "Q"
    if card == 13: card = "K"
    if card == 14: card = "A"
    hand.append(card)
    return hand


def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')


def print_results(dealer_hand, player_hand):
    clear()

    print("\n    WELCOME TO BLACKJACK!\n")
    print("-" * 30 + "\n")
    print("    \033[1;32;40mWINS:  \033[1;37;40m%s   \033[1;31;40mLOSSES:  \033[1;37;40m%s\n" % (wins, losses))
    print("-" * 30 + "\n")
    print("The dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)))
    print("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))


def blackjack(dealer_hand, player_hand):
    global wins
    global losses
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Congratulations! You got a Blackjack!\n")
        wins += 1
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Sorry, you lose. The dealer got a blackjack.\n")
        losses += 1
        play_again()


def score(dealer_hand, player_hand):
    global wins
    global losses
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Congratulations! You got a Blackjack!\n")
        wins += 1
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Sorry, you lose. The dealer got a blackjack.\n")
        losses += 1
    elif total(player_hand) > 21:
        print_results(dealer_hand, player_hand)
        print("Sorry. You busted. You lose.\n")
        losses += 1
    elif total(dealer_hand) > 21:
        print_results(dealer_hand, player_hand)
        print("Dealer busts. You win!\n")
        wins += 1
    elif total(player_hand) < total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("Sorry. Your score isn't higher than the dealer. You lose.\n")
        losses += 1
    elif total(player_hand) > total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("Congratulations. Your score is higher than the dealer. You win\n")
        wins += 1


def game():
    global wins
    global losses
    choice = 0
    clear()
    print("\n    WELCOME TO BLACKJACK!\n")
    print("-" * 30 + "\n")
    print("    \033[1;32;40mWINS:  \033[1;37;40m%s   \033[1;31;40mLOSSES:  \033[1;37;40m%s\n" % (wins, losses))
    print("-" * 30 + "\n")
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    print("The dealer is showing a " + str(dealer_hand[0]))
    print("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
    blackjack(dealer_hand, player_hand)
    quit = False
    while not quit:
        choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
        if choice == 'h':
            hit(player_hand)
            print(player_hand)
            print("Hand total: " + str(total(player_hand)))
            if total(player_hand) > 21:
                print('You busted')
                losses += 1
                play_again()
        elif choice == 's':
            while total(dealer_hand) < 17:
                hit(dealer_hand)
                print(dealer_hand)
                if total(dealer_hand) > 21:
                    print('Dealer busts, you win!')
                    wins += 1
                    play_again()
            score(dealer_hand, player_hand)
            play_again()
        elif choice == "q":
            print("Bye!")
            quit = True
            exit()


if __name__ == "__main__":
    game()
 