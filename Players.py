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
    for player in tournament.players:
        if player.lastname == entry_winner_name:
            player.add_point(1)


def egalite(tournament, entry_winner_name, entry_loser_name):
    for player in tournament.players:
        if player.lastname == entry_winner_name:
            player.add_point(0.5)
    for player in tournament.players:
        if player.lastname == entry_loser_name:
            player.add_point(0.5)


def ajout_rang(tournament, entry_lastname, entry_rank):
    for player in tournament.players:
        if player.lastname == entry_lastname:
            player.rank_update(entry_rank)
