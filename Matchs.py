class Matchs:
    def __init__(self, player1, player2):
        self.tuplematch = ([player1, 0], [player2, 0])

    def player1_win(self):
        self.tuplematch[0][1] = 1

    def player2_win(self):
        self.tuplematch[1][1] = 1

    def draw(self):
        self.tuplematch[0][1] = 0.5
        self.tuplematch[1][1] = 0.5