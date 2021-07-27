# Importing all of the necessary functions from other files to use
from engfunctions import engblackjack, engrules
from frfunctions import frblackjack, frrules
from esfunctions import esblackjack, esrules


class LangError(Exception):  # Exception that is raised if the user does not enter a valid language.
    pass  # Pass statement acts as an empty line basically. Does not do anything the console just passes through it


# Adv. Technique No. 3 - Define function.
def lang_select():
    # The whole thing is in a while loop so it will keep repeating to ask the user until they enter a valid response.
    while True:
        try:
            lang = input(
                "\nSelect a Language / Sélectionnez une Langue / Selecciona un Idioma:\nEnglish\nFrançais\nEspañol\n")
            lang = lang.strip()  # Stripping and lowering the input to make it easier for the user to enter
            lang = lang.lower()  # Adv. Technique 1 (String manipulation)

            if lang == "english" or lang == "eng" or lang == "en":
                print("English selected.")
                engrules()
                engblackjack()
                break  # Runs the game and then breaks out of the loop when the user enters a valid response.
            elif lang == "francais" or lang == "fr" or lang == "f" or lang == "français" or lang == "french":
                print("French selected.")
                frrules()
                frblackjack()
                break
            elif lang == "espanol" or lang == "es" or lang == "spanish" or lang == "español":
                print("Español selected.")
                esrules()
                esblackjack()
                break
            else:
                raise LangError
        except LangError:  # Exception is raised when the user does not enter a valid response, then repeats loop.
            print("Please enter a valid language / Veuillez entrer une langue valide / Ingrese un idioma válido")
