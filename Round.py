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
