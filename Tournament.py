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

    def first_round(self):
        tri = sorted(self.players, key=lambda player: player.rank)
        # renvoie une liste de joueur trié par rang
