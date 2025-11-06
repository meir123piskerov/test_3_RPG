import random
from core.player import Player
from core.orc import *
from core.goblin import *


class Game:
    @staticmethod
    def start(name):
        type_of_player = ["worrier", "healer"]
        player = Player(name, randint(5, 10), randint(5, 10), randint(5, 15), type_of_player[randint(0, 1)])
        return player

    def show_menu(self):
        return "fight / exit"

    @staticmethod
    def choose_random_monster(name):
        monster1 = Orc(name)
        monster2 = Goblin(name)
        type_of_monster = [monster1, monster2]
        return type_of_monster[random.randint(0, 1)]

    def battle(self, player: Player, monster: Orc):
        pass

    @staticmethod
    def roll_dice():
        return random.randint(6, 20)

    @staticmethod
    def speed_for_first_move(player: Player, monster: Orc, roll):
        player.speed += roll
        monster.speed += roll

    @staticmethod
    def first_move(player: Player, monster: Orc):
        if player.speed >= monster.speed:
            return True
        else:
            return False

    @staticmethod
    def attack(attacker: Player, defender: Orc, roll):
        if attacker.speed + roll > defender.armor_rating:
            return "hit"
        else:
            return "miss"

    @staticmethod
    def damage(attacker: Player, defender: Orc, roll):
        attacker.power += roll
        if defender.type == "orc" or defender.type == "goblin":
            if defender.weapon == "knife":
                defender.hp -= (attacker.power * 0.5)
            elif defender.weapon == "sword":
                defender.hp -= attacker.power
            elif defender.weapon == "axe":
                defender.hp -= (attacker.power * 1.5)


        else:
            defender.hp -= attacker.power

    @staticmethod
    def status(player: Player):
        return player.hp
