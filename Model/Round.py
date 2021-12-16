from typing import List
from datetime import datetime
from Model.Matchs import Matchs


class Round:
    def __init__(self, matchs: List[Matchs], name):
        self.end = None
        self.name = name
        self.matchs = matchs
        self.creation = datetime.now()

    def end_round(self):
        self.end = datetime.now()

    def serialize(self):
        serialized_matchs_list = [match.serialize() for match in self.matchs]
        return {
            "creation": str(self.creation),
            "name": self.name,
            "match": serialized_matchs_list,
            "end": str(self.end)
        }

    @staticmethod
    def load(json):
        return Round([Matchs.load(match)
                      for match in json["match"]], json["match"])
