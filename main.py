from core.orc import *
from game import Game

if __name__ == "__main__":
    player_choice = input(" 1: to start the game : \n 2: to exit the game :", )
    if player_choice == "1":
        player = Game.start("meir")
        monster = Game.choose_random_monster("bob")
        print("HP:", player.hp, 'Profession:', player.profession, 'Speed:', player.speed, 'Power:', player.power)
        print("HP:", monster.hp, 'Type:', monster.type, 'Power:', player.power, "Weapon:", monster.weapon)
        Game.speed_for_first_move(player, monster, randint(0, 6))
        player_move = Game.first_move(player, monster)
        monster_move = not (Game.first_move(player, monster))
        player_flag = player_move
        monster_flag = monster_move

        if player_flag:
            print("Player starts!")
        else:
            print("Monster starts!")
        while player.hp >= 0 and monster.hp >= 0:

            while player_flag:

                if Game.attack(player, monster, Game.roll_dice()) == "hit":
                    Game.damage(player, monster, randint(0, 6))
                player_flag = not player_flag
                monster_flag = not monster_flag

            while monster_flag:

                if Game.attack(monster, player, Game.roll_dice()):
                    Game.damage(monster, player, randint(0, 6))
                player_flag = not player_flag
                monster_flag = not monster_flag

        if player.hp > monster.hp:
            print("player won")
        else:
            print("monster won")
    else:
        print("exit game")
