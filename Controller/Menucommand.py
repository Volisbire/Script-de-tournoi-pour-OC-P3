import Vue
from PawnPatrol import PawnPatrol
from Players import Player


# ce controller recupere les inputs pour PawnPatrol.py,et appel la DB, instance de Players

class Menu:
    def __init__(self, control: PawnPatrol, testmode):
        self.control = control
        self.testmode = testmode

    def show(self):
        Vue.welcome()
        if self.start_or_load_tournament() == "S":
            self.create_player()
            self.register_tournament()
        else:
            Vue.hop()
            self.load_tournament()

        for i in range(self.control.get_remaining_rounds()):
            self.next_round()
            self.show_round(i)
            self.ask_match_result(i)
        Vue.saut_de_ligne()
        self.print_players()

    def create_player(self):
        if self.testmode:
            self.control.fake_players()
            return
        player_number = 8
        Vue.hop()
        for i in range(int(player_number)):
            self.control.add_player(self.players_data(i))

    def players_data(self, player_number):
        Vue.print_player_number(player_number)
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
        Vue.saut_de_ligne_deux()
        for match in self.control.get_match_round(round):
            print(match.get_player1().lastname + "  versus  " + match.get_player2().lastname)
        self.a_tout_moment()

    def ask_match_result(self, round):
        Vue.hop()
        for match in self.control.get_match_round(round):
            print(match.get_player1().lastname + "  versus  " + match.get_player2().lastname)
            winner = input("Veuillez entrer le nom du joueur ayant gagné "
                           "(entrez n'importe quoi d'autre en cas d'égalité): ")
            Vue.saut_de_ligne_trois()
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
        Vue.pretty_saut_de_ligne()
        self.a_tout_moment()

    def a_tout_moment(self):
        Vue.saut_de_ligne_deux()
        choice = input("Voulez vous changer le rang d'un joueur ? O ""\n"
                       "Sauvegarder/charger un tournoi ? S/L ""\n"
                       "Afficher la liste des joueurs du tournoi en cours par ordre alpabetique/classement ? A/R""\n"
                       "Afficher le rapport d'un tournoi ? T""\n"
                       "Céer le tournoi ? K""\n"
                       "Pour continuer le tournoi appuyer sur entrée""\n")
        if choice == "O":
            Vue.hop()
            joueur = input("Veuillez indiquer le nom du joueur : ")
            rank = input("Veuillez indiquer le rang souhaité : ")
            for player in self.control.player_list:
                if joueur == player.lastname:
                    player.rank = rank
        if choice == "S":
            Vue.tournament_saved()
            self.control.save()
        if choice == "L":
            self.load_tournament()
        if choice == "A":
            sorted_alpha_list = self.control.sorted_alpha_list()
            Vue.print_sorted_alpha_list(sorted_alpha_list)
            self.a_tout_moment()
        if choice == "R":
            sorted_rank_list = self.control.sorted_byrank_list()
            Vue.print_sorted_rank_list(sorted_rank_list)
            self.a_tout_moment()
        if choice == "T":
            self.rapport()
        if choice == "K":
            self.register_tournament()

    def rapport(self):
        tournament_list = self.control.tournament_list()
        n = 0
        for _ in tournament_list:
            Vue.print_tournament_list(tournament_list, n)
            n += 1
        tournament_id_choice = input("Entrez l'ID du tounoi souhaité : ")
        report_choice = input("Quel type de rapport souhaitez vous voir ?""\n"
                              "Rapport complet du tournoi ? R""\n"
                              "Liste des joueurs par ordre alphabetique/classement ? A/C""\n"
                              "Liste des rounds du tournoi ? L""\n"
                              "Liste des matchs du tournoi ? M""\n"
                              "Appuer sur entrée pour poursuivre le tournoi""\n")
        if report_choice == "R":
            tournament_json = self.control.get_tournament(int(tournament_id_choice))
            Vue.print_tournament_name(tournament_json)
            for round in tournament_json["rounds"]:
                Vue.print_round_name(round)
                for index_match, match in enumerate(round["match"]):
                    Vue.print_index_match(index_match, round["match"])
            self.a_tout_moment()
        if report_choice == "A":
            tournament_json = self.control.get_tournament(int(tournament_id_choice))
            affichage = (self.control.get_alpha_list(tournament_json))
            Vue.print_get_alpha_list(affichage)
            self.a_tout_moment()
        if report_choice == "C":
            tournament_json = self.control.get_tournament(int(tournament_id_choice))
            affichage = (self.control.get_ranked_list(tournament_json))
            Vue.print_get_ranked_list(affichage)
            self.a_tout_moment()
        if report_choice == "L":
            tournament_json = self.control.get_tournament(int(tournament_id_choice))
            affichage = (self.control.get_round_list(tournament_json))
            Vue.print_get_round_list(affichage)
            self.a_tout_moment()
        if report_choice == "M":
            tournament_json = self.control.get_tournament(int(tournament_id_choice))
            affichage = (self.control.get_match_list(tournament_json))
            Vue.print_get_match_list(affichage)
            self.a_tout_moment()

    def start_or_load_tournament(self):
        return input("Voulez vous charger(L)/commencer(S) un tournoi  ? L/S""\n")

    def load_tournament(self):
        tournament_list = self.control.tournament_list()
        n = 0
        for _ in tournament_list:
            Vue.print_tournament_list(tournament_list, n)
            n += 1
        tournament_id_choice = input("Entrez l'ID du tounoi souhaité : ")
        tournament_json = self.control.get_tournament(int(tournament_id_choice))
        Vue.tournament_loaded()
        self.control.load(tournament_json)
