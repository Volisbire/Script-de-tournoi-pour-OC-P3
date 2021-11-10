from Players import fake_players
from Tournament import Tournoi
from Matchs import Matchs
from Round import Round


def bullet_start():
    print("Go ")
    jo = fake_players()
    jolito = jo.values()
    tournoi = Tournoi("tournoi de ouf", "Paris", "21/07/81", jolito, "10:10", "bogoss")
    first_matchs_list = tournoi.match_list_by_rank()
    first_round = Round(first_matchs_list, "Round 1")
    n = 0
    result = Matchs(first_matchs_list[n].firstname, first_matchs_list[n+4].firstname)
    winner = input("Indiquez le nom du joueur ayant gagné : ")
    if winner == first_matchs_list[n].firstname:
        result.player1_win()
    elif winner == first_matchs_list[n+4].firstname:
        result.player2_win()
    else:
        result.draw()
    n += 1
    print(first_matchs_list[n].firstname)
    print(first_round.name, first_round.creation)
    print(result.tuplematch)


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
