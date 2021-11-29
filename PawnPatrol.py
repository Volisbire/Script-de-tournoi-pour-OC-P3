from tinydb import TinyDB

from Tournament import *

db = TinyDB("db.json")


class Playerlist:
    def __init__(self):
        self.player_list = []

    def add_player(self, entry_lastname, entry_firstname, entry_birth, entry_sex, entry_rank):
        self.player_list.append(Player(entry_lastname, entry_firstname, entry_birth, entry_sex, entry_rank))


players = Playerlist()


def registered_tournament(entry_tournament_name, entry_place, entry_dated,
                          entry_tournament_type_string, entry_comments):
    player_list = players.player_list
    tournament = Tournoi(entry_tournament_name, entry_place, entry_dated, player_list,
                         entry_tournament_type_string, entry_comments)


def start_tournament_():
    print("tapar")


def add_point_(entry_winner_name):
    pass
