def welcome():
    print(" =============================== ")
    print(" Bienvenue dans Chess.Tournament ")
    print(" =============================== ")
    print("")
    print("")


def saut_de_ligne():
    print("")
    print("")
    print("")
    print(" ==================== ")


def print_player_number(player_nbr):
    player_number = int(player_nbr)
    print(f"Veuillez entrer les informations du joueur {player_number + 1} :")


def saut_de_ligne_deux():
    print("")
    print(" ================= ")
    print("")


def saut_de_ligne_trois():
    print("")
    print(" ================ ")


def pretty_saut_de_ligne():
    print(" ================= ")
    print("")


def tournament_saved():
    print("")
    print("Tournoi sauvegardé.")
    print(" ================= ")
    print("")


def tournament_loaded():
    print("")
    print("Tournoi chargé.")
    print(" ================= ")
    print("")


def hop():
    print("")


def print_tournament_list(tournament_list, n):
    print(tournament_list[n]["name"] + " " + str(n + 1))


def print_tournament_name(tournament_json):
    print("Tournament name : " + tournament_json["name"])


def print_round_name(round):
    print(round["name"])
    print("")
    print("")


def print_index_match(index_match, match):
    print(" ================= ")
    print("Match " + str(index_match + 1))
    print(match["player1"]["firstname"] + " " + match["player1"]["lastname"])
    print(match["player1"]["point"])
    print(match["player2"]["firstname"] + " " + match["player2"]["lastname"])
    print(match["player2"]["point"])
    print(" ================= ")
    print("\n")


def print_sorted_alpha_list(sorted_alpha_list):
    print(sorted_alpha_list)


def print_sorted_rank_list(rank_list):
    print(rank_list)


def print_get_alpha_list(affichage):
    print(affichage)


def print_get_ranked_list(affichage):
    print(affichage)


def print_get_round_list(affichage):
    print(affichage)


def print_get_match_list(affichage):
    print(affichage)


def print_match(match):
    print(match.get_player1().lastname + "  versus  "
          + match.get_player2().lastname)


def print_player_point(player):
    print("    ", player.lastname, "  ", player.point)
