class Player:
    def __init__(self, lastname, firstname, birth, sex, rank):
        self.lastname = lastname
        self.firstname = firstname
        self.birth = birth
        self.sex = sex
        self.rank = rank
        self.point = 0

    def serialize(self):
        return {"lastname": self.lastname,
                "firstname": self.firstname,
                "birth": self.birth,
                "sex": self.sex,
                "rank": self.rank,
                "point": self.point
                }

    def rank_update(self, rank):
        self.rank += int(rank)

    def add_point(self, point):
        self.point += int(point)


def ajout_point(tournament, entry_winner_name):
    n = 0
    for _ in tournament.players:
        if tournament.players[n].lastname == entry_winner_name:
            tournament.players[n].add_point(1)
        n += 1


def egalite(tournament, entry_winner_name, entry_loser_name):
    n = 0
    for _ in tournament.players:
        if tournament.players[n].lastname == entry_winner_name:
            tournament.players[n].add_point(0.5)
        n += 1
    n = 0
    for _ in tournament.players:
        if tournament.players[n].lastname == entry_loser_name:
            tournament.players[n].add_point(0.5)
        n += 1


def ajout_rang(tournament, entry_lastname, entry_rank):
    n = 0
    for _ in tournament.players:
        if tournament.players[n].lastname == entry_lastname:
            tournament.players[n].rank_update(entry_rank)
        n += 1
