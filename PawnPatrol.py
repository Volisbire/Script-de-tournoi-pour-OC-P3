from tkinter import Tk, Label, LabelFrame

from tinydb import TinyDB

from Players import ajout_point, egalite, ajout_rang
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
    global tournament
    tournament = Tournoi(entry_tournament_name, entry_place, entry_dated, player_list,
                         entry_tournament_type_string, entry_comments)


def add_point_(entry_winner_name):
    ajout_point(tournament, entry_winner_name)


def draw_(entry_winner_name, entry_loser_name):
    egalite(tournament, entry_winner_name, entry_loser_name)


def update_rank_(entry_lastname, entry_rank):
    ajout_rang(tournament, entry_lastname, entry_rank)


def start_tournament_():
    tournament.next_round()
    r = len(tournament.rounds)-1
    m = 0
    print(r)
    player1 = tournament.rounds[m].match[r].tuplematch[0][0].lastname
    player2 = tournament.rounds[m].match[r].tuplematch[1][0].lastname
    app = Tk()
    app.geometry('600x400')
    app.title("Chess tournament v1.0.0.1")
    lol = LabelFrame(app, text="Match "+str(len(tournament.rounds)), padx=20, pady=20)
    lol.pack(fill="both", expand="yes")

    Label(lol, text=str(player1)+" Versus "+str(player2)).pack()

    app.mainloop()
