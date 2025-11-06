import random
from random import randint


class Orc:
    weapon = ["knife", "axe", "sword"]

    def __init__(self, name):
        self.name = name
        self.hp = 50
        self.type = "Orc"
        self.speed = random.randint(0, 5)
        self.power = random.randint(10, 15)
        self.armor_rating = random.randint(2, 8)
        self.weapon = Orc.weapon[random.randint(0, 2)]

    def speak(self):
        return f'the angry {self.name}'

    def attack(self):
        pass
