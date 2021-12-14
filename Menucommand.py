
from PawnPatrol import PawnPatrol
from Players import Player


class Menu:
    def __init__(self, control: PawnPatrol, testmode):
        self.control = control
        self.testmode = testmode

    def show(self):
        print(" =============================== ")
        print(" Bienvenue dans Chess.Tournament ")
        print(" =============================== ")
        print("")
        print("")
        self.create_player()
        self.register_tournament()

        for i in range(self.control.get_round_number()):
            self.next_round()
            self.show_round(i)
            self.ask_match_result(i)
        print("")
        print("")
        print("")
        print(" ==================== ")
        self.print_players()

    def create_player(self):
        if self.testmode:
            self.control.fake_players()
            return
        player_number = 8
        print("")
        for i in range(int(player_number)):
            self.control.add_player(self.players_data(i))

    def players_data(self, player_number):
        print(f"Veuillez entrer les informations du joueur {player_number + 1} :")
        return Player(input("Nom : "), input("Prenom : "), input("Date de naissance : "), input("Sexe : "),
                      input("Rang : "))

    def register_tournament(self):
        self.control.register_tournament(input("Veuillez renseigner le nom du tournoi : "),
                                         input("Veuillez renseigner la lieu du tournoi : "),
                                         input("Veuillez renseigner la date du tournoi : "),
                                         input("Veuillez renseigner le type de tournoi : "),
                                         input("Des commentaires : "))

    def next_round(self):
        self.control.next_round()

    def show_round(self, round):
        print("")
        print(" ================= ")
        print("")
        for match in self.control.get_match_round(round):
            print(match.get_player1().lastname + "  versus  " + match.get_player2().lastname)
        self.a_tout_moment()

    def ask_match_result(self, round):
        print("")
        for match in self.control.get_match_round(round):
            print(match.get_player1().lastname + "  versus  " + match.get_player2().lastname)
            winner = input("Veuillez entrer le nom du joueur ayant gagné "
                           "(entrez n'importe quoi d'autre en cas d'égalité): ")
            print("")
            print(" ================ ")
            if winner == match.get_player1().lastname:
                match.player1_win()
            elif winner == match.get_player2().lastname:
                match.player2_win()
            else:
                match.draw()
        self.control.fin_de_tour()
        self.a_tout_moment()

    def print_players(self):
        for player in self.control.player_list:
            print("    ", player.lastname, "  ", player.point)
        print(" ================= ")
        print("")
        self.a_tout_moment()

    def a_tout_moment(self):
        print("")
        print(" ================= ")
        print("")
        choice = input("Voulez vous changer le rang d'un joueur ? O ""\n"
                       "Sauvegarder/charger un tournoi ? S/L ""\n"
                       "Afficher la liste des joueurs du tournoi en cours par ordre alpabetique/classement ? A/R""\n"
                       "Afficher le rapport d'un tournoi ? T""\n"
                       "Pour continuer le tournoi, appuyer sur la touche Entrée""\n")
        if choice == "O":
            print("")
            joueur = input("Veuillez indiquer le nom du joueur : ")
            rank = input("Veuillez indiquer le rang souhaité : ")
            for player in self.control.player_list:
                if joueur == player.lastname:
                    player.rank = rank
        if choice == "S":
            print("")
            print("Tournoi sauvegardé.")
            print(" ================= ")
            print("")
            self.control.save()
        if choice == "L":
            print("")
            print("Tournoi chargé.")
            print(" ================= ")
            print("")
            self.control.load()
        if choice == "A":
            print(self.control.sorted_alpha_list())
        if choice == "R":
            print(self.control.sorted_byrank_list())
        if choice == "T":
            tournament_list = self.control.tournament_list()
            n = 0
            for _ in tournament_list:
                print(tournament_list[n]["name"] + " " + str(n + 1))
                n += 1
            tournament_id_choice = input("Entrez l'ID du tounoi souhaité : ")
            report_choice = input("Quel type de rapport souhaitez vous voir ?""\n"
                                  "Rapport complet du tournoi ? R""\n"
                                  "Liste des joueurs par ordre alphabetique/classement ? A/C""\n"
                                  "Liste des rounds du tournoi ? L""\n"
                                  "Liste des matchs du tournoi ? M""\n")
            if report_choice == "R":
                tournament_json = self.control.get_tournament(int(tournament_id_choice))
                print("Tournament name : " + tournament_json["name"])
                for round in tournament_json["rounds"]:
                    print(round["name"])
                    print("")
                    print("")
                    for index_match, match in enumerate(round["match"]):
                        print(" ================= ")
                        print("Match " + str(index_match + 1))
                        print(match["player1"]["firstname"] + " " + match["player1"]["lastname"])
                        print(match["player1"]["point"])
                        print(match["player2"]["firstname"] + " " + match["player2"]["lastname"])
                        print(match["player2"]["point"])
                        print(" ================= ")
                    print("\n")
            if report_choice == "A":
                tournament_json = self.control.get_tournament(int(tournament_id_choice))
                print(self.control.get_alpha_list(tournament_json))
            if report_choice == "C":
                tournament_json = self.control.get_tournament(int(tournament_id_choice))
                print(self.control.get_ranked_list(tournament_json))
            if report_choice == "L":
                tournament_json = self.control.get_tournament(int(tournament_id_choice))
                print(self.control.get_round_list(tournament_json))
            if report_choice == "M":
                tournament_json = self.control.get_tournament(int(tournament_id_choice))
                print(self.control.get_match_list(tournament_json))


        if choice == "W":
            print(self.control.tournament_rounds_list())
            # a revoir
        if choice == "M":
            print(self.control.tournament_match_list())
