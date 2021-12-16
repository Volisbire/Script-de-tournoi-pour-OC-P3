class Player:
    def __init__(self, lastname, firstname, birth, sex, rank, point=0):
        self.lastname = lastname
        self.firstname = firstname
        self.birth = birth
        self.sex = sex
        self.rank = rank
        self.point = point

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

    @staticmethod
    def load(json):
        return Player(json["lastname"], json["firstname"],
                      json["birth"], json["sex"], json["rank"], json["point"])
