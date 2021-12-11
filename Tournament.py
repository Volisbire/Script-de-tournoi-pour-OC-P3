
from typing import List
from Matchs import Matchs
from Players import Player
from Round import Round


class Tournoi:
    def __init__(self, name, place, dated, players: List[Player], time_, desc, nbrturns=4):
        self.name = name
        self.place = place
        self.dated = dated
        self.nbrturns = nbrturns
        self.players = players
        self.time_ = time_
        self.desc = desc
        self.rounds: List[Round] = []
        # ajouter une method qui get la list des ID joueurs dans TinyDB

    def match_list_by_rank(self) -> List[Matchs]:
        sorted_by_rank = sorted(self.players, key=lambda player: player.rank)
        return self.create_match_list(sorted_by_rank)

    def match_list_by_point(self) -> List[Matchs]:
        sorted_by_point = sorted(self.players, key=lambda player: player.point)
        return self.create_match_list(sorted_by_point)

    @staticmethod
    def create_match_list(player_list):
        match_list = []
        for i in range(int(len(player_list) / 2)):
            match_list.append(Matchs(player_list[i], player_list[i + 3]))
        return match_list

    def next_round(self):
        round_number = len(self.rounds) + 1
        if round_number == 1:
            match_list = self.match_list_by_rank()
        else:
            match_list = self.match_list_by_point()
        new_round = Round(match_list, "round :" + str(round_number))
        self.rounds.append(new_round)

    def serialize(self):
        serialized_players_list = [player.serialize() for player in self.players]
        serialized_rounds_list = [round.serialize() for round in self.rounds]
        return {"name": self.name,
                "place": self.place,
                "dated": self.dated,
                "nbrturns": self.nbrturns,
                "players": serialized_players_list,
                "time": str(self.time_),
                "desc": self.desc,
                "rounds": serialized_rounds_list
                }
