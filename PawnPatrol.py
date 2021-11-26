from Players import Player
from tinydb import TinyDB, Query

from Tournament import Tournoi

db = TinyDB("db.json")
registred_player = []


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


def registered_tournament(entry_tournament_name, entry_place, entry_dated,
                          entry_tournament_type_string, entry_comments):
    player_list = []
    for i in range(6):
        player_object = db.get(doc_id=i + 1)
        lastname = player_object["lastname"]
        firstname = player_object["firstname"]
        birth = player_object["birth"]
        sex = player_object["sex"]
        rank = player_object["rank"]
        player_object = Player(lastname, firstname, birth, sex, rank)
        player_list.append(player_object)
    print(player_list[0].lastname)

    tournament = Tournoi(entry_tournament_name, entry_place, entry_dated, player_list,
                         entry_tournament_type_string, entry_comments)
    print(tournament.players)


def start_tournament_():
    print("tapar")


def add_point_(entry_winner_name, entry_loser_name):
    print(entry_winner_name)
    print(entry_loser_name)

