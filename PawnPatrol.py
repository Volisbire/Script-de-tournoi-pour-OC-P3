from Players import Player
from tinydb import TinyDB, Query

db = TinyDB("db.json")


def register_player(entry_lastname, entry_firstname, entry_birth, entry_sex, entry_rank):
    player = {"lastname": entry_lastname,
              "firstname": entry_firstname,
              "birth": entry_birth,
              "sex": entry_sex,
              "rank": entry_rank,
              "point": 0
              }
    db.insert(player)
    return Player(player["lastname"], player["firstname"], player["birth"], player["sex"],
                  player["rank"])
