from tinydb import TinyDB, Query
import Players
from Players import *
from Tournament import *
from Menu import *

db = TinyDB("db.json")
# player_dict = {}
# player_list = []
print("===============================")
print("*    Bonjour et bienvenue :)  *")
print("===============================")
print("")
# for i in range(2):
#     player_dict.update(players_data(i + 1))
#     print("")
# player_dict = player_dict.values()
player_dict = Players.fake_players().values()
print(player_dict)
# player_list = []
# for i in player_dict:
#     player_list.append((i.serialize()))
# for i in player_list:
#     db.insert(player_list[i])
# tournament_type = menu()
# if tournament_type == "1":
#     bullet_start(player_dict)
