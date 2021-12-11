from typing import List
from datetime import datetime
from Matchs import Matchs


class Round:
    def __init__(self, matchs: List[Matchs], name):
        self.end = None
        self.name = name
        self.matchs = matchs
        self.creation = datetime.now()

    def end_round(self):
        self.end = datetime.now()

    def serialize(self):
<<<<<<< HEAD
        serialized_matchs_list = [match.serialize() for match in self.matchs]
        return {
            "end": str(self.end),
            "name": self.name,
            "match": serialized_matchs_list,
            "creation": str(self.creation)
=======
        serialized_matchs_list = []
        for i in self.match:
            serialized_matchs_list.append(i.serialize())
        return {
            "end": self.end,
            "name": self.name,
            "match": self.match,
            "creation": self.creation
>>>>>>> 17c924e6aa425a64d787b0b8205140ca5211cfb7
        }
