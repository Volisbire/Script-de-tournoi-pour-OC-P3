from typing import List

from Players import Player


class Tournoi:
    def __init__(self, name, place, dated, players: List[Player], time_, desc, nbrturns=4):
        self.name = name
        self.place = place
        self.dated = dated
        self.nbrturns = nbrturns
        self.players = players
        self.time_ = time_
        self.desc = desc

    def match_list_by_rank(self):
        return sorted(self.players, key=lambda player: player.rank)

    def match_list_by_point(self):
        return sorted(self.players, key=lambda player: player.point, reverse=True)
