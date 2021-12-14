from typing import List
from tinydb import TinyDB
from tinydb import Query
from Matchs import Matchs
from Players import Player
from Tournament import Tournoi


class PawnPatrol:
    def __init__(self):
        self.player_list = []
        self.tournament: Tournoi
        self.db = TinyDB("ChessTournament.json", indent=4)
        self.player_table = self.db.table("Players")
        self.tournament_table = self.db.table("Tournament")

    def add_player(self, player):
        self.player_list.append(player)
        self.player_table.insert(player.serialize())

    def register_tournament(self, entry_tournament_name, entry_place, entry_dated,
                            entry_tournament_type_string, entry_comments):
        player_list = self.player_list
        self.tournament = Tournoi(entry_tournament_name, entry_place, entry_dated, player_list,
                                  entry_tournament_type_string, entry_comments)

    def next_round(self):
        self.tournament.next_round()

    def fake_players(self):
        self.player_list = [Player("john1", "titor1", "210781", "M", 8),
                            Player("john2", "titor2", "210781", "M", 2),
                            Player("john3", "titor3", "210781", "M", 3),
                            Player("john4", "titor4", "210781", "M", 4),
                            Player("john5", "titor5", "210781", "M", 5),
                            Player("john6", "titor6", "210781", "M", 6),
                            Player("john7", "titor7", "210781", "M", 7),
                            Player("john8", "titor8", "210781", "M", 1)
                            ]

    def get_match_round(self, round_number) -> List[Matchs]:
        return self.tournament.rounds[round_number].matchs

    def get_round_number(self):
        return self.tournament.nbrturns

    def save(self):
        self.tournament_table.insert(self.tournament.serialize())

    def fin_de_tour(self):
        self.tournament.rounds[len(self.tournament.rounds) - 1].end_round()

    def load(self):
        pass

    def sorted_alpha_list(self):
        sorted_alpha_list = []
        for player in self.player_list:
            sorted_alpha_list.append(player.firstname)
        sorted_alpha_list = sorted(sorted_alpha_list)
        return sorted_alpha_list

    def sorted_byrank_list(self):
        sorted_rank_list = []
        for player in self.player_list:
            sorted_rank_list.append((player.lastname, player.rank))
        sorted_rank_list.sort(key=lambda x: x[1])
        return sorted_rank_list

    def get_tournament(self, tournament_id_choice):
        return self.tournament_table.get(doc_id=tournament_id_choice)

    def tournament_rounds_list(self):
        query = Query()
        return self.tournament_table.search(query.creation.matches("[aZ]*"))

    def tournament_match_list(self):
        pass


    def tournament_list(self):
        return self.tournament_table.all()

    def get_alpha_list(self, tournament_json):
        alpha_list = []
        for player in tournament_json["players"]:
            alpha_list.append(player["firstname"])
        return sorted(alpha_list)

    def get_ranked_list(self, tournament_json):
        ranked_list = []
        for player in tournament_json["players"]:
            ranked_list.append((player["firstname"], player["point"]))
        ranked_list.sort(key=lambda x: x[1])
        return ranked_list

    def get_round_list(self, tournament_json):
        round_list = []
        for round in tournament_json["rounds"]:
            round_list.append(round["name"])
        return round_list

    def get_match_list(self, tournament_json):
        match_list = []
        for round in tournament_json["rounds"]:
            for match in round["match"]:
                match_list.append((match["player1"]["lastname"] + match["player1"]["firstname"],
                                   match["player2"]["lastname"] + match["player2"]["firstname"]))
        return match_list
