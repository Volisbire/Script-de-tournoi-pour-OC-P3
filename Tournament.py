
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
<<<<<<< HEAD
        serialized_players_list = [player.serialize() for player in self.players]
        serialized_rounds_list = [round.serialize() for round in self.rounds]

=======
        serialized_list = []
        for i in self.players:
            serialized_list.append(i.serialize())
        serialized_rounds_list = []
        for _ in self.rounds:
            n = 0
            for i in self.rounds[n].match:
                serialized_rounds_list.append(i.serialize())
                n += 1
>>>>>>> 17c924e6aa425a64d787b0b8205140ca5211cfb7
        return {"name": self.name,
                "place": self.place,
                "dated": self.dated,
                "nbrturns": self.nbrturns,
<<<<<<< HEAD
                "players": serialized_players_list,
                "time": str(self.time_),
=======
                "players": serialized_list,
                "time": self.time_,
>>>>>>> 17c924e6aa425a64d787b0b8205140ca5211cfb7
                "desc": self.desc,
                "rounds": serialized_rounds_list
                }
