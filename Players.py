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
