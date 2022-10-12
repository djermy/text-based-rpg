import render

class Player:
    max_hp = 100
    def __init__(self, name, gender, xp, max_hp, health, fatigue, defence, strength, speed, intelligence):
        self.name = name
        self.gender = gender
        self.xp = xp
        self.max_hp = max_hp
        self.health = health
        self.fatigue = fatigue
        self.defence = defence
        self.strength = strength
        self.speed = speed
        self.intelligence = intelligence

    def display_player_bar(self, xp, max_hp, health, fatiegue):
        # print health
        print("HP: ", end="")
        render.print_bar(self.health, self.max_hp)
        print("\n" + "FT: ", end="")
        render.print_bar(self.fatigue, 100)
        print()


# Lv. 34 (XP: 1024/2000)
# HP: [=======      ]     50/100
# FT: [=============]    100/100