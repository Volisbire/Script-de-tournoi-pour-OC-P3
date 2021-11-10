from typing import List
from datetime import datetime


class Round:
    def __init__(self, match: List[Match], name):
        self.end = None
        self.name = name
        self.creation = datetime.now()

    def end_round(self):
        self.end = datetime.now()
