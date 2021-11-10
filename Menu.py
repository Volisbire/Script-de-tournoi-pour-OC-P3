from Players import *
from Tournament import *


def bullet_start():
    joueurs_en_lice = players_dictionnary()
    premier_tri(joueurs_en_lice)
    print("GO !")


def blitz_start():
    pass


def rapid_strike():
    pass


def menu():
    print("Bonjour, veuillez indiquer le type de tournoi :")
    print("1. Bullet")
    print("2. Blitz")
    print("3. Coup rapide")
    tournament_type = input("Entrez un nombre entre 1 et 3 : ")
    if tournament_type == "1":
        bullet_start()
    elif tournament_type == "2":
        blitz_start()
    elif tournament_type == "3":
        rapid_strike()
    else:
        menu()

    return tournament_type


menu()
gagnant = input("indiquer le numéro du joueur l'ayant emporte (ex: 1 pour le joueur 1): ")
