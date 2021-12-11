import Players


class Matchs:
    def __init__(self, player1: Players, player2: Players):
        self.tuplematch = ([player1, 0], [player2, 0])

    def player1_win(self):
        self.get_player1().add_point(1)
        self.tuplematch[0][1] = 1

    def get_player1(self):
        return self.tuplematch[0][0]

    def player2_win(self):
        self.get_player2().add_point(1)
        self.tuplematch[1][1] = 1

    def get_player2(self):
        return self.tuplematch[1][0]

    def draw(self):
        self.get_player1().add_point(0.5)
        self.get_player2().add_point(0.5)
        self.tuplematch[0][1] = 0.5
        self.tuplematch[1][1] = 0.5

    def serialize(self):
        return {
            "player1": self.get_player1().serialize(),
            "player1points": self.tuplematch[0][1],
            "player2": self.get_player2().serialize(),
            "player2points": self.tuplematch[1][1]
        }
