import random
import textwrap
import math  # Importing some built-in python libraries that I need for my code.

dealervalue = int()
playervalue = int()
dealernew = str()
playernew = str()
play = str()
ace = 0
dealerace = 0
dealertotal = int()
playertotal = int()  # Defining all of the values used in the code

# List of deck of cards that is modified throughout the game
cards = ["K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2", "A", "K", "Q", "J", "10", "9", "8", "7", "6", "5",
         "4", "3", "2", "A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2", "A", "K", "Q", "J", "10", "9",
         "8", "7", "6", "5", "4", "3", "2", "A"]

dealerhand = []
playerhand = []  # The dealer and player's hand is an empty list to start with


def dealercheck():   # Check the value of the dealers new card and adds it to their total
    global dealertotal, dealerace, dealervalue  # Allowing the values to be used globally outside of this module
    dealervalue = int(0)

    if dealerace == -10:    # If the dealer's ace switched values on their last move, this resets the value so
        dealerace = 0       # they don't lose 10 off of their total every move.

    if dealernew == "K" or dealernew == "Q" or dealernew == "J":  # Face cards are worth 10
        dealervalue += 10
    elif dealernew == "A" and dealertotal + 11 > 21:
        dealerace = 1
    elif dealernew == "A" and dealertotal + 11 <= 21:
        dealerace = 11
    elif dealernew == "A" and "A" in dealerhand:   # Deciding if the ace is worth 11 or 1
        dealertotal += 1
    elif dealernew == "2":
        dealervalue += 2
    elif dealernew == "3":
        dealervalue += 3
    elif dealernew == "4":
        dealervalue += 4
    elif dealernew == "5":
        dealervalue += 5
    elif dealernew == "6":
        dealervalue += 6
    elif dealernew == "7":
        dealervalue += 7
    elif dealernew == "8":
        dealervalue += 8
    elif dealernew == "9":
        dealervalue += 9
    elif dealernew == "10":
        dealervalue += 10

    if ace == 11 and dealertotal + dealervalue > 21:  # Ace switching values if the dealer goes over 21.
        dealerace = -10
        dealertotal += dealerace

    if dealernew == "A":
        dealertotal += dealerace

    dealertotal += dealervalue  # Adding the new card's value to the total score.


def dealerdeal():
    global dealerhand
    global dealernew

    # Adv. Technique 1, Modifying data stored in collection.
    dealernew = random.choice(cards)  # Using external library random to choose a random card from the deck.
    cards.remove(dealernew)           # Removing the card from the list of cards.
    dealerhand.append(dealernew)      # Appending the new card to the dealers list of cards.
    dealercheck()                     # Checking value of new card.


def playercheck():   # Same as the dealercheck() but it is for the player's hand.
    global playertotal, ace, playervalue
    playervalue = int(0)

    if ace == -10:
        ace = 0

    if playernew == "K" or playernew == "Q" or playernew == "J":
        playervalue += 10
    elif playernew == "A" and playertotal + 11 > 21:
        ace = 1
    elif playernew == "A" and playertotal + 11 < 21:
        ace = 11
    elif playernew == "A" and playertotal + 11 == 21:
        ace = 11
    elif playernew == "A" and "A" in playerhand:
        playertotal += 1
    elif playernew == "2":
        playervalue += 2
    elif playernew == "3":
        playervalue += 3
    elif playernew == "4":
        playervalue += 4
    elif playernew == "5":
        playervalue += 5
    elif playernew == "6":
        playervalue += 6
    elif playernew == "7":
        playervalue += 7
    elif playernew == "8":
        playervalue += 8
    elif playernew == "9":
        playervalue += 9
    elif playernew == "10":
        playervalue += 10

    if ace == 11 and playertotal + playervalue > 21:
        ace = -10
        playertotal += ace

    if playernew == "A":
        playertotal += ace

    playertotal += playervalue


def playerdeal():  # Same as the dealerdeal() but it is for the player
    global playerhand
    global playernew
    playernew = random.choice(cards)
    cards.remove(playernew)
    playerhand.append(playernew)
    playercheck()


chips = 1000  # The amount of chips that the user starts with to bet


class BetError(Exception):
    pass


bet = 0  # Resetting the users bet each round.


def engbetting():
    global chips, bet

    bet = 0

    while True:
        try:
            print("\nYou have", chips, "chips")  # Returning value of total chips remaining.
            bet = int(input("How many chips would you like to bet?\n"))
            if bet > chips or bet < 1:  # If the user enters a number of chips that is invalid it raises an error
                raise BetError
            break
        except BetError:
            print("You must enter a whole number between one and the amount of chips you currently have.\n")
        except ValueError:  # If the user does not enter a number it raises this error.
            print("That's not a number!")

    print()
    print(bet, "chips betted. If you win you will receive", bet * 2, "chips.")  # String manipulation


class EngChoiceError(Exception):
    pass


def engdisplay():  # Function that displays the current cards on the table and the total of each player.
    print("\nDealer:", dealertotal, "\n", dealerhand)
    print("\nYou:", playertotal, "\n", playerhand)


class EngPlayError(Exception):
    pass


class NoChips(Exception):
    pass


def engplayagain():  # Asking the user if they would like to play again.
    global play
    while True:
        try:
            play = input("\nWould you like to play another round? Yes/No\n")
            play = play.strip()
            play = play.lower()
            if chips == 0:  # If the user has no chips they can't bet so they have to stop playing.
                raise NoChips
            if play == "no" or play == "n":
                print("\nThanks for playing!")
                quit()  # Quits the program
            elif play == "yes" or play == "y":
                engreset()         # Resets cards list and playerhand/dealerhand list
                engblackjack()     # Starts game again
                break
            else:
                raise EngPlayError
        except EngPlayError:
            print("\nPlease enter Yes or No.")
        except NoChips:
            print("\nYou don't have any chips left. Better luck next time!")
            quit()


def engnatural():  # Runs if the player gets dealt 21.
    global chips, bet
    if playertotal == 21:
        engdisplay()
        print("Blackjack! You Win!")
        chips += math.floor(int(bet * 3/2))  # math.floor rounds down the value to the nearest integer so no decimal
        print("You won", math.floor(int(bet * 3/2)), "chips. Now you have", chips, "chips."
              "(Natural Blackjack = 1.5x chips)")
        engplayagain()  # Asks if the user wants to play another round.
    else:
        pass


def dealerstand():  # If the dealer stands, do they win or lose?
    global chips, bet
    engdisplay()
    if dealertotal < playertotal:  # If lower than player total, player wins.
        print("Dealer stands on ", dealertotal, ".", " You win!", sep="")
        chips += bet  # Adds the bet to the users total chips
        print("You won", bet * 2, "chips. Now you have", chips, "chips.")
    elif dealertotal > playertotal:  # If greater than player total, player loses.
        print("Dealer stands on ", dealertotal, ".", " You lose!", sep="")
        chips -= bet  # Subtracts the bet from the users total chips
        print("You lost", bet, "chips. Now you have", chips, "chips.")
    elif dealertotal == playertotal:  # If equal to player total, draw.
        print("Dealer stands on", dealertotal, ".", "It's a draw!")
        print("You get your bet back, you now have", chips, "chips.")  # Total chips does not change


class DealerBusted(Exception):
    pass


def engdealer21():
    global chips, bet, dealertotal
    while True:
        try:
            if dealertotal == 21:
                engdisplay()
                print("Dealer stands on 21. You Lose!")
                chips -= bet
                print("You lost", bet, "chips. Now you have", chips, "chips.")
                break
            elif dealertotal > 21:
                raise DealerBusted
            elif dealertotal >= 17:
                dealerstand()
                break
            elif dealertotal < 17:
                dealerdeal()
        except DealerBusted:  # If dealer goes over 21, player wins.
            engdisplay()
            print("\nDealer busted!")
            chips += bet
            print("You won", bet * 2, "chips. Now you have", chips, "chips.")
            break


class ActionError(Exception):
    pass


def engchoice():  # Allows the user to choose what move they would like to make.
    global bet
    while True:
        try:
            engdisplay()
            while True:
                try:
                    action = input("Would you like to Hit or Stand?\n")
                    action = action.lower()
                    action = action.strip()
                    if action == "hit" or action == "h" or action == "s" or action == "stand":
                        break
                    else:
                        raise EngChoiceError
                except EngChoiceError:
                    print("Please enter Hit or Stand.\n")

            if action == "hit" or action == "h":
                playerdeal()
                engplayer21()
                if playertotal < 21:  # If the player hits and does not bust, they can hit or stand again.
                    engchoice()
                break
            elif action == "stand" or action == "s":  # If player stands, they cannot hit anymore and the dealer goes
                raise ActionError
        except ActionError:
            break


def engplayer21():
    global chips, bet, playertotal

    if playertotal == 21:   # If player hits to 21, does not necessarily win because the dealer can draw the game
        engdealer21()
    elif playertotal > 21:  # If player goes over 21, they bust and lose their bet.
        engdisplay()
        print("\nYou busted!")
        chips -= bet
        print("You lost", bet, "chips.", "You now have", chips, "chips.")
        engplayagain()
    else:
        pass


def engreset():  # Setting all the values back to their default
    global playerhand, dealerhand, playertotal, dealertotal, cards
    playerhand = []
    dealerhand = []
    playertotal = 0
    dealertotal = 0
    cards = ["K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2", "A", "K", "Q", "J", "10", "9", "8", "7", "6",
             "5", "4", "3", "2", "A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2", "A", "K", "Q", "J",
             "10", "9", "8", "7", "6", "5", "4", "3", "2", "A"]


class RuleError(Exception):
    pass


def engrules():  # Displays once at the start of the program for people for have not played before.
    while True:
        try:
            rule_choice = input("\nWould you like to read the rules of Blackjack? Yes/No\n")
            rule_choice = rule_choice.strip()
            rule_choice = rule_choice.lower()
            if rule_choice == "yes" or rule_choice == "y":
                print(textwrap.dedent("""
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                The aim of Blackjack is to end up with a total higher than the dealers, while remaining under
                21. On your turn you will be presented with two options - Hit and Stand.
                
                If you hit, you will receive another card and the value of that card will be added to your total. You
                can hit as many times as you would like in a round until you stand or bust.
                
                If you stand, you will not make any more moves and the dealer now has their chance to hit or stand. The
                dealer must stand on a total 17 or higher. 
                
                Numbered cards 2 through 10 are worth their numeric value, face cards are all worth 10. An ace is worth 
                11 but will switch to being worth 1 if you go over 21.
                
                If your total goes over 21, you bust and lose your bet. If you have a total higher than the dealer, or
                the dealer busts, you win double your bet. If you are dealt 21, you receive 1.5x your bet.
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                """))
                break
            elif rule_choice == "no" or rule_choice == "n":
                break
            else:
                raise RuleError
        except RuleError:
            print("Please enter Yes or No.")


def engstart():  # Start of the game. Betting, and beginning deal.
    engbetting()
    dealerdeal()
    playerdeal()
    playerdeal()


def engblackjack():         # Main function, entire game is in this function.
    while True:
        engstart()          # User bets and the cards get dealt
        engnatural()        # Checks if the user got dealt 21
        engchoice()         # User hits or stands
        engdealer21()       # Dealer hits or stands
        while True:
            engplayagain()  # If they want to play again, loops. If not, ends program.
