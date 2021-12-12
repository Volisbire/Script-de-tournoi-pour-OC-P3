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
        player_number = input("Combien de joueurs vont participer  : ")
        print("")
        for i in range(int(player_number)):
            self.control.add_player(self.players_data(i))

    def players_data(self, player_number):
        print(f"Entrez les informations du joueur {player_number + 1} :")
        print(f"Veuillez entrer les informations du joueur {player_number + 1} :")
        player = Player(input("Nom : "), input("Prenom : "), input("Date de naissance : "), input("Sexe : "),
                      input("Rang : "))
        PLayers.save(player)
        return player

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
        choice = input("Voulez vous changer le rang d'un joueur ? O "
                       "Voulez vous sauvegarder/charger un tournoi ? S/L ")
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
