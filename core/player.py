class Player:
    def __init__(self, name, speed, power, armor_rating, profession, hp=50):
        self.name = name
        self.speed = speed
        self.power = power
        self.armor_rating = armor_rating
        self.profession = profession
        self.hp = hp
        self.type = ''

    def check(self):
        if self.profession == "healer":
            self.hp += 10
        elif self.profession == "worrier":
            self.power += 2

    def speak(self):
        return self.name

    def attack(self):
        pass
