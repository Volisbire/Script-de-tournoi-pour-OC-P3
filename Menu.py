from Tournament import Tournoi
from Matchs import Matchs
from Round import Round


def bullet_start(player_dict):
    print("C'est parti pour un bullet !")
    print("")
    print("Veuillez entrer les informations necessaires a la creation du tournoi :")

    tournament = Tournoi(input("nom: "), input("L'endroit: "), input("La date: "), player_dict, input("L'heure: "),
                         input("Des commentaires ? "))
    first_matchs_list = tournament.match_list_by_rank()
    print(first_matchs_list)
    first_round = Round(first_matchs_list, "Round 1")
    n = 0
    result = Matchs(first_matchs_list[n].firstname, first_matchs_list[n + 4].firstname)
    print("")
    print("=====================================")
    print("")
    print(f"{first_matchs_list[n].firstname}, affronte {first_matchs_list[n + 4].firstname}")
    print("")
    winner = input("Indiquez le nom du joueur ayant gagné le match "
                   "(entrez n'importe quoi d'autre en cas d'égalité): ")
    if winner == first_matchs_list[n].firstname:
        result.player1_win()
    elif winner == first_matchs_list[n + 4].firstname:
        result.player2_win()
    else:
        result.draw()
    n += 1
    print("")
    print("----------------------------------")
    print(first_round.name, first_round.creation)
    print("----------------------------------")
    print(result.tuplematch[0][0], result.tuplematch[0][1])
    print(result.tuplematch[1][0], result.tuplematch[1][1])


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
    if tournament_type not in ["1", "2", "3"]:
        menu()
    return tournament_type
