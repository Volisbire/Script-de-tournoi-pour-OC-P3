class Match:
    def __init__(self, player1, player2):
        self.tupledeouf = ([player1, 0], [player2, 0])

    def win_player1(self):
        self.tupledeouf[0][1] = 1

    def win_player2(self):
        self.tupledeouf[1][1] = 1

    def draw(self):
        self.tupledeouf[0][1] = 0.5
        self.tupledeouf[1][1] = 0.5
