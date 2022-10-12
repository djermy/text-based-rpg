import render
import util

class Player:
    max_hp = 100
    def __init__(self, name, gender, xp, max_hp, health, fatigue, defence, strength, speed, intelligence):
        self.name = name
        self.gender = gender
        self.level = util.calculate_current_level(xp)
        self.xp = xp
        self.max_hp = max_hp
        self.health = health
        self.fatigue = fatigue
        self.defence = defence
        self.strength = strength
        self.speed = speed
        self.intelligence = intelligence

    def display_player_bar(self):
        current_level = util.calculate_current_level(self.xp)
        required_xp = util.xp_required_for_level(current_level + 1)
        print("LV. " + str(current_level) + " (XP: " + str(self.xp) + "/" + str(required_xp) + ")", end="")

        # print health
        print()
        print("HP: ", end="")
        render.print_bar(self.health, self.max_hp)
        
        # print fatigue
        print()
        print("FT: ", end="")
        render.print_bar(self.fatigue, 100)
        print()


# Lv. 34 (XP: 1024/2000)
# HP: [=======      ]     50/100
# FT: [=============]    100/100