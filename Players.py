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
                "rank": self.rank
                }

    def add_point(self, point):
        self.point += point


def players_data(player_number):
    print(f"Entrez les informations du joueur {player_number} :")
    player = {f"joueur {player_number}": (
        Player(input("Nom : "), input("Prenom : "), input("Date de naissance : "), input("Sexe : "),
               input("Rang : ")))}
    return player


def fake_players():
    fauxjoueurs = {"John": Player("john", "titor", "210781", "M", 1),
                   "Johty": Player("john", "titor", "210781", "M", 2),
                   "Johnas": Player("john", "titor", "210781", "M", 3),
                   "Johnneu": Player("john", "titor", "210781", "M", 4),
                   "Johnnou": Player("john", "titor", "210781", "M", 5),
                   "JohnWayne": Player("john", "titor", "210781", "M", 6),
                   "Jolastico": Player("john", "titor", "210781", "M", 7),
                   "Jopleinletuyo": Player("john", "titor", "210781", "M", 8)
                   }
    return fauxjoueurs


def players_dictionnary():
    nombre_de_joueur = 2
    dict_de_joueur = {}
    for i in range(nombre_de_joueur):
        dict_de_joueur.update(players_data(i + 1))
    return dict_de_joueur
