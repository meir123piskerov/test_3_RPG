import random


class Goblin:
    weapon = ["knife", "axe", "sword"]

    def __init__(self, name):
        self.name = name
        self.hp = 20
        self.type = "goblin"
        self.speed = random.randint(5, 10)
        self.power = random.randint(5, 10)
        self.armor_rating = 1
        self.weapon = Goblin.weapon[random.randint(0, 2)]

    def speak(self):
        return f'the angry {self.name}'

    def attack(self):
        pass


