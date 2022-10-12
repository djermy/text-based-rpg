import render
import util

class Player:
    max_hp = 100
    def __init__(self, name, gender, level, xp, max_hp, health, fatigue, defence, strength, speed, intelligence):
        self.name = name
        self.gender = gender
        self.level = level
        self.xp = xp
        self.max_hp = max_hp
        self.health = health
        self.fatigue = fatigue
        self.defence = defence
        self.strength = strength
        self.speed = speed
        self.intelligence = intelligence

    def display_player_bar(self, level, xp, max_hp, health, fatigue):
        # print xp/level
        print("LV. " + str(util.calculate_current_level(self.xp)) + " (XP: " + str(self.xp) + "/" + str(round(util.xp_required_for_level(self.level))) + ")", end="")

        # print health
        print("\n" + "HP: ", end="")
        render.print_bar(self.health, self.max_hp)
        
        # print fatigue
        print("\n" + "FT: ", end="")
        render.print_bar(self.fatigue, 100)
        print()


# Lv. 34 (XP: 1024/2000)
# HP: [=======      ]     50/100
# FT: [=============]    100/100