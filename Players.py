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

    def add_point(self, point):
        self.point += point

    def rank_update(self, rank):
        self.rank += rank


def players_data(player_number):
    print(f"Veuillez entrer les informations du joueur {player_number} :")
    player = {f"joueur {player_number}": (
        Player(input("Nom : "), input("Prenom : "), input("Date de naissance : "), input("Sexe : "),
               input("Rang : ")))}
    return player


def fake_players():
    fauxjoueurs = {"Player1": Player("john1", "titor1", "210781", "M", 8),
                   "Player2": Player("john2", "titor2", "210781", "M", 2),
                   "Player3": Player("john3", "titor3", "210781", "M", 3),
                   "Player4": Player("john4", "titor4", "210781", "M", 4),
                   "Player5": Player("john5", "titor5", "210781", "M", 5),
                   "Player6": Player("john6", "titor6", "210781", "M", 6),
                   "Player7": Player("john7", "titor7", "210781", "M", 7),
                   "Player8": Player("john8", "titor8", "210781", "M", 1)
                   }
    return fauxjoueurs


def players_dictionnary():
    nombre_de_joueur = 2
    dict_de_joueur = {}
    for i in range(nombre_de_joueur):
        dict_de_joueur.update(players_data(i + 1))
    return dict_de_joueur
