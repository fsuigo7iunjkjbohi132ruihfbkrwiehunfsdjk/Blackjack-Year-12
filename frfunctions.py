# All comments are written on engfunctions.py ~ This code is the same just in French.
import math
import random
import textwrap

dealervalue = int()
playervalue = int()
dealernew = str()
playernew = str()
play = str()
ace = 0
dealerace = 0
dealertotal = int()
playertotal = int()

cards = ["K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2", "A", "K", "Q", "J", "10", "9", "8", "7", "6", "5",
         "4", "3", "2", "A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2", "A", "K", "Q", "J", "10", "9",
         "8", "7", "6", "5", "4", "3", "2", "A"]

dealerhand = []
playerhand = []


def dealercheck():
    global dealertotal, dealerace, dealervalue
    dealervalue = int(0)

    if dealerace == -10:
        dealerace = 0

    if dealernew == "K" or dealernew == "Q" or dealernew == "J":
        dealervalue += 10
    elif dealernew == "A" and dealertotal + 11 > 21:
        dealerace = 1
    elif dealernew == "A" and dealertotal + 11 < 21:
        dealerace = 11
    elif dealernew == "A" and dealertotal + 11 == 21:
        dealerace = 11
    elif dealernew == "A" and "A" in dealerhand:
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

    if ace == 11 and dealertotal + dealervalue > 21:
        dealerace = -10
        dealertotal += dealerace

    if dealernew == "A":
        dealertotal += dealerace

    dealertotal += dealervalue


def dealerdeal():
    global dealerhand
    global dealernew
    dealernew = random.choice(cards)
    cards.remove(dealernew)
    dealerhand.append(dealernew)
    dealercheck()


def playercheck():
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


def playerdeal():
    global playerhand
    global playernew
    playernew = random.choice(cards)
    cards.remove(playernew)
    playerhand.append(playernew)
    playercheck()


class BetError(Exception):
    pass


chips = 1000  # The amount of chips that the user is betting each round
bet = 0


def frbetting():
    global chips, bet
    # The amount of chips that the user has to bet
    bet = 0

    while True:
        try:
            print("\nVous avez", chips, "jetons")
            bet = int(input("Combien de jetons souhaitez-vous miser?\n"))
            if bet > chips or bet < 1:
                raise BetError
            break
        except BetError:
            print("Vous devez saisir un nombre entier compris entre un et le nombre de jetons dont vous disposez "
                  "actuellement.\n")
        except ValueError:
            print("Ce n'est pas un chiffre!")

    print()
    print(bet, "jetons misés. Si vous gagnez, vous recevrez", bet * 2, "jetons.")


def playerstand():
    pass


class FrChoiceError(Exception):
    pass


def frdisplay():
    print("\nCroupier:", dealertotal, "\n", dealerhand)
    print("\nVous:", playertotal, "\n", playerhand)


class FrPlayError(Exception):
    pass


class NoChips(Exception):
    pass


def frplayagain():
    global play
    while True:
        try:
            play = input("\nSouhaitez-vous jouer un autre tour? Oui/Non\n")
            play = play.strip()
            play = play.lower()
            if chips == 0:
                raise NoChips
            if play == "non" or play == "n":
                print("\nMerci d'avoir joué!")
                quit()
            elif play == "oui" or play == "o":
                frreset()
                frblackjack()
                break
            else:
                raise FrPlayError
        except FrPlayError:
            print("\nVeuillez saisir Oui ou Non.")
        except NoChips:
            print("\nVous n'avez plus de jetons. Plus de chance la prochaine fois!")
            quit()


def frnatural():
    global chips, bet
    if playertotal == 21:
        frdisplay()
        print("Vingt-et-Un! Vous gagnez!")
        chips += math.floor(int(bet * 3 / 2))
        print("Vous avez gagné", math.floor(int(bet * 3 / 2)), "jetons. Vous avez maintenant", chips,
              "jetons. (Naturel Vingt-et-Un = 1,5x jetons)")
        frplayagain()
    else:
        pass


def dealerstand():
    global chips, bet
    frdisplay()
    if dealertotal < playertotal:
        print("Le croupier reste sur ", dealertotal, ".", " Vous gagnez!", sep="")
        chips += bet
        print("Vous avez gagné", bet * 2, "jetons. Vous avez maintenant", chips, "jetons.")
    elif dealertotal > playertotal:
        print("Le croupier reste sur ", dealertotal, ".", " Vous perdez!", sep="")
        chips -= bet
        print("Vous avez perdu", bet, "jetons. Vous avez maintenant", chips, "jetons.")
    elif dealertotal == playertotal:
        print("Le croupier reste sur ", dealertotal, ".", "C'est une égalité!")
        print("Vous récupérez votre mise, vous avez maintenant", chips, "jetons.")


class DealerBusted(Exception):
    pass


def frdealer21():
    global chips, bet, dealertotal
    while True:
        try:
            if dealertotal == 21:
                frdisplay()
                print("Le croupier reste sur 21. Vous perdez!")
                chips -= bet
                print("Vous avez perdu", bet, "jetons. Vous avez maintenant", chips, "jetons.")
                break
            elif dealertotal > 21:
                raise DealerBusted
            elif dealertotal >= 17:
                dealerstand()
                break
            elif dealertotal < 17:
                dealerdeal()
        except DealerBusted:
            frdisplay()
            print("\nLe croupier avez sauté!")
            chips += bet
            print("Vous avez gagné", bet * 2, "jetons. Vous avez maintenant", chips, "jetons.")
            break


class ActionError(Exception):
    pass


def frchoice():
    global bet
    while True:
        try:
            frdisplay()
            while True:
                try:
                    action = input("Voulez-vous tirer ou rester?\n")
                    action = action.lower()
                    action = action.strip()
                    if action == "tirer" or action == "t" or action == "rester" or action == "r":
                        break
                    else:
                        raise FrChoiceError
                except FrChoiceError:
                    print("Veuillez saisir tirer ou rester.\n")

            if action == "tirer" or action == "t":
                playerdeal()
                frplayer21()
                if playertotal < 21:
                    frchoice()
                break
            elif action == "rester" or action == "r":
                raise ActionError
        except ActionError:
            break


def frplayer21():
    global chips, bet, playertotal

    if playertotal == 21:
        frdealer21()
    elif playertotal > 21:
        frdisplay()
        print("\nVous avez sauté!")
        chips -= bet
        print("Vous avez perdu", bet, "jetons.", "Vous avez maintenant", chips, "jetons.")
        frplayagain()
    else:
        pass


def frreset():
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


def frrules():
    while True:
        try:
            rule_choice = input("\nAimeriez-vous lire les règles du Vingt-et-Un? Oui/Non\n")
            rule_choice = rule_choice.strip()
            rule_choice = rule_choice.lower()
            if rule_choice == "oui" or rule_choice == "o":
                print(textwrap.dedent("""
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Le but du Blackjack est de se retrouver avec un total supérieur à celui des croupiers, tout en restant
                sous 21. À votre tour, deux options vous seront présentées: Tirer et Rester.

                Si vous tirez, vous recevrez une autre carte et la valeur de cette carte sera ajoutée à votre total. Toi
                pouvez tirer autant de fois que vous le souhaitez en un tour jusqu'à ce que vous soyez debout ou sauté.

                Si vous restez, vous ne ferez plus aucun mouvement et le concessionnaire a maintenant sa chance de tirer
                ou de rester. Le revendeur doit rester sur un total de 17 ou plus.

                Les cartes numérotées de 2 à 10 valent leur valeur numérique, les figures valent toutes 10. Un as vaut
                11 mais passera à 1 si vous dépassez 21.

                Si votre total dépasse 21, vous sautez et perdez votre pari. Si vous avez un total supérieur à celui du 
                croupier, ou le croupier saute, vous gagnez le double de votre mise. Si vous recevez 21, vous recevez 
                1,5 fois votre mise.
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                """))
                break
            elif rule_choice == "non" or rule_choice == "n":
                break
            else:
                raise RuleError
        except RuleError:
            print("Veuillez entrer Oui ou Non.")


def frstart():
    frbetting()
    dealerdeal()
    playerdeal()
    playerdeal()


def frblackjack():
    global play
    while True:
        frstart()
        frnatural()
        frchoice()
        frdealer21()
        while True:
            frplayagain()
