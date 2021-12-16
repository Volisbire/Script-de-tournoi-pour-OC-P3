from typing import List
from Model.Matchs import Matchs
from Model.Players import Player
from Model.Round import Round


class Tournoi:
    def __init__(self, name, place, dated, players: List[Player],
                 time_, desc, nbrturns=4):
        self.name = name
        self.place = place
        self.dated = dated
        self.nbrturns = nbrturns
        self.players = players
        self.time_ = time_
        self.desc = desc
        self.rounds: List[Round] = []

    def match_list_by_rank(self) -> List[Matchs]:
        sorted_by_rank = \
            sorted(self.players,
                   key=lambda player: player.rank, reverse=True)
        return self.create_pair_list(sorted_by_rank)

    def match_list_by_point(self) -> List[Matchs]:
        sorted_by_point = \
            sorted(self.players,
                   key=lambda player: [(-player.point), player.rank],
                   reverse=True)
        return self.create_next_round(sorted_by_point)

    def create_pair_list(self, player_list):
        group_first = player_list[:len(player_list) // 2]
        group_second = player_list[len(player_list) // 2:]
        return self.create_first_round(group_first, group_second)

    def create_first_round(self, group_first, group_second):
        # cascade depuis la fonction match_list_by_rank
        match_list = []
        for player1, player2 in zip(group_first, group_second):
            match_list.append(Matchs(player1, player2))
        return match_list

    def create_next_round(self, sorted_by_point):
        # cascade depuis la fonction sorted_by_points
        lastname_players_list = []
        match_list = []
        player1 = 0
        player2 = 1
        for player in sorted_by_point:
            lastname_players_list.append(player.lastname)
        for i in range(len(lastname_players_list) - 1):
            if not \
                self.already_played_together(lastname_players_list[player1],
                                             lastname_players_list[player2]):
                match_list.append(Matchs(sorted_by_point[player1],
                                         sorted_by_point[player2]))
                if len(match_list) == 4:
                    return match_list
            player1 += 1
            player2 += 1
        return match_list

    def already_played_together(self, player1, player2):
        # verification des pairs déja joué
        # dans l'objet instancié
        for round in self.rounds:
            for match in round.matchs:
                if ((player1, player2) == (match.get_player1().lastname,
                                           match.get_player2().lastname) or
                        (player1, player2) == (match.get_player2().lastname,
                                               match.get_player1().lastname)):
                    return True
        return False

    def next_round(self):
        # method appelée pour la creation d'un round,
        # appele une fonction pour le premier,
        # une autre pour les suivants
        round_number = len(self.rounds) + 1
        if round_number == 1:
            match_list = self.match_list_by_rank()
        else:
            match_list = self.match_list_by_point()
        new_round = Round(match_list, "round :" + str(round_number))
        self.rounds.append(new_round)

    def serialize(self):
        serialized_players_list = [player.serialize()
                                   for player in self.players]
        serialized_rounds_list = [round.serialize()
                                  for round in self.rounds]

        return {"name": self.name,
                "place": self.place,
                "dated": self.dated,
                "nbrturns": self.nbrturns,
                "players": serialized_players_list,
                "time": str(self.time_),
                "desc": self.desc,
                "rounds": serialized_rounds_list
                }

    @staticmethod
    def load(tournament_json):
        tournoi_load = \
            Tournoi(tournament_json["name"], tournament_json["place"],
                    tournament_json["dated"],
                    [Player.load(player) for
                     player in tournament_json["players"]],
                    tournament_json["time"],
                    tournament_json["desc"])
        tournoi_load.rounds = [Round.load(round) for
                               round in tournament_json["rounds"]]
        return tournoi_load
