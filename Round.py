from typing import List
from datetime import datetime
from Matchs import Matchs


class Round:
    def __init__(self, match: List[Matchs], name):
        self.end = None
        self.name = name
        self.match = match
        self.creation = datetime.now()

    def end_round(self):
        self.end = datetime.now()

    def serialize(self):
        serialized_matchs_list = []
        for i in self.match:
            serialized_matchs_list.append(i.serialize())
        return {
            "end": self.end,
            "name": self.name,
            "match": self.match,
            "creation": self.creation
        }
