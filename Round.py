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
        serialized_matchs_list = []
        for match in self.matchs:
            serialized_matchs_list.append(match.serialize())
        return {
            "end": self.end,
            "name": self.name,
            "match": self.matchs,
            "creation": self.creation
        }
