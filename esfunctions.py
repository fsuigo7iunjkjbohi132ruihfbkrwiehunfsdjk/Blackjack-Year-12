# All comments are written on engfunctions.py ~ This code is the same just in Spanish.
import math
import random
import textwrap

dealervalue = int()
playervalue = int()
dealernew = str()
playernew = str()
dealertotal = int()
playertotal = int()
play = str()

cards = ["K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2", "A", "K", "Q", "J", "10", "9", "8", "7", "6", "5",
         "4", "3", "2", "A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2", "A", "K", "Q", "J", "10", "9",
         "8", "7", "6", "5", "4", "3", "2", "A"]

dealerhand = []
playerhand = []

dealerace = 0


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


ace = 0


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


chips = 1000
bet = 0


def esbetting():
    global chips, bet
    bet = 0

    while True:
        try:
            print("\nTienes", chips, "fichas.")
            bet = int(input("¿Cuántas fichas te gustaría apostar?\n"))
            if bet > chips or bet < 1:
                raise BetError
            break
        except BetError:
            print("Debes ingresar un número entero entre uno y la cantidad de fichas que tienes actualmente.\n")
        except ValueError:
            print("¡Eso no es un número!")

    print()
    print(bet, "fichas apostadas. Si gana, recibirá", bet * 2, "fichas.")


def playerstand():
    pass


class EsChoiceError(Exception):
    pass


def esdisplay():
    print("\nEl Crupier:", dealertotal, "\n", dealerhand)
    print("\nTú:", playertotal, "\n", playerhand)


class EsPlayError(Exception):
    pass


class NoChips(Exception):
    pass


def esplayagain():
    global play
    while True:
        try:
            play = input("\n¿Le gustaría jugar otra ronda? Sí/No\n")
            play = play.strip()
            play = play.lower()
            if chips == 0:
                raise NoChips
            if play == "no" or play == "n":
                print("\n¡Gracias por jugar!")
                quit()
            elif play == "si" or play == "s" or play == "sí":
                esreset()
                esblackjack()
                break
            else:
                raise EsPlayError
        except EsPlayError:
            print("\n")
        except NoChips:
            print("\nNo te quedan fichas. ¡Mejor suerte la próxima vez!")
            quit()


def esnatural():
    global chips, bet
    if playertotal == 21:
        esdisplay()
        print("Veintiuna! ¡Tú ganas!")
        chips += math.floor(int(bet * 3 / 2))
        print("Ganaste", math.floor(int(bet * 3 / 2)), "fichas, ahora tienes", chips,
              "fichas. (Veintiuna natural = 1.5x fichas)")
        esplayagain()
    else:
        pass


def dealerstand():
    global chips, bet
    esdisplay()
    if dealertotal < playertotal:
        print("Crupier se queda en ", dealertotal, ".", " ¡Tú ganas!", sep="")
        chips += bet
        print("Ganaste", bet * 2, "fichas. Ahora tienes", chips, "fichas.")
    elif dealertotal > playertotal:
        print("Crupier se queda en ", dealertotal, ".", " ¡Pierdes!", sep="")
        chips -= bet
        print("Perdiste", bet, "fichas. Ahora tienes", chips, "fichas.")
    elif dealertotal == playertotal:
        print("Crupier se queda en ", dealertotal, ".", " ¡Es un empate!", sep="")
        print("Recupera tu apuesta. Ahora tienes", chips, "fichas.")


class DealerBusted(Exception):
    pass


def esdealer21():
    global chips, bet, dealertotal
    while True:
        try:
            if dealertotal == 21:
                esdisplay()
                print("El crupier se queda en 21. ¡Pierdes!")
                chips -= bet
                print("Perdiste", bet, "fichas. Ahora tienes", chips, "fichas.")
                break
            elif dealertotal > 21:
                raise DealerBusted
            elif dealertotal >= 17:
                dealerstand()
                break
            elif dealertotal < 17:
                dealerdeal()
        except DealerBusted:
            esdisplay()
            print("\nCrupier se pasa!")
            chips += bet
            print("Ganaste", bet * 2, "fichas. Ahora tienes", chips, "fichas.")
            break


class ActionError(Exception):
    pass


def eschoice():
    global bet
    while True:
        try:
            esdisplay()
            while True:
                try:
                    action = input("¿Te gustaría Carta o Plantarse?\n")
                    action = action.lower()
                    action = action.strip()
                    if action == "carta" or action == "c" or action == "plantarse" or action == "p":
                        break
                    else:
                        raise EsChoiceError
                except EsChoiceError:
                    print("Ingrese Carta o Plantarse.\n")

            if action == "carta" or action == "c":
                playerdeal()
                esplayer21()
                if playertotal < 21:
                    eschoice()
                break
            elif action == "plantarse" or action == "p":
                raise ActionError
        except ActionError:
            break


def esplayer21():
    global chips, bet, playertotal

    if playertotal == 21:
        esdealer21()
    elif playertotal > 21:
        esdisplay()
        print("\n¡Te rompiste!")
        chips -= bet
        print("Perdiste", bet, "fichas.", "Ahora tienes", chips, "fichas.")
        esplayagain()
    else:
        pass


def esreset():
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


def esrules():
    while True:
        try:
            rule_choice = input("\n¿Le gustaría leer las reglas del Blackjack? Sí/No\n")
            rule_choice = rule_choice.strip()
            rule_choice = rule_choice.lower()
            if rule_choice == "si" or rule_choice == "s" or rule_choice == "sí":
                print(textwrap.dedent("""
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                El objetivo del Blackjack es terminar con un total superior al de los crupieres, sin dejar de
                21. En su turno, se le presentarán dos opciones: pedir y plantarse.

                Si aciertas, recibirás otra carta y el valor de esa carta se sumará a tu total. Tú
                puede golpear tantas veces como desee en una ronda hasta que se pare o se rompa.

                Si se planta, no hará más movimientos y el crupier ahora tiene la oportunidad de pedir o plantarse. La
                el crupier debe estar en un total de 17 o más.

                Las cartas numeradas del 2 al 10 valen su valor numérico, las cartas con figuras valen todas 10. Un as 
                vale 11, pero pasará a valer 1 si superas los 21.

                Si su total supera los 21, se pasa y pierde su apuesta. Si tiene un total más alto que el distribuidor, 
                o el crupier se arruina, usted gana el doble de su apuesta. Si recibe 21, recibe 1,5 veces su apuesta.
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                """))
                break
            elif rule_choice == "no" or rule_choice == "n":
                break
            else:
                raise RuleError
        except RuleError:
            print("Por favor ingrese Sí o No")


def esstart():
    esbetting()
    dealerdeal()
    playerdeal()
    playerdeal()


def esblackjack():
    global play
    while True:
        esstart()
        esnatural()
        eschoice()
        esdealer21()
        while True:
            esplayagain()
