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
        self.rank += rank

    def add_point(self, point):
        self.point += point



def ajout_rang(tournament, entry_lastname, entry_rank):
    for player in tournament.players:
        if player.lastname == entry_lastname:
            player.rank_update(entry_rank)
