import render
import util

class Player:
    max_hp = 100
    def __init__(self, name, gender, xp, max_hp, health, fatigue, defence, strength, speed, intelligence):
        self.name = name
        self.gender = gender
        self.xp = xp
        self.level = util.calculate_current_level(xp)
        self.max_hp = max_hp
        self.health = health
        self.fatigue = fatigue
        self.defence = defence
        self.strength = strength
        self.speed = speed
        self.intelligence = intelligence
        self.inventory = []
    

    def print_player_stats(self):
        print()
        print(self.name)
        print()
        print("You are: " + self.gender)
        print("You are level: " + str(self.level))
        print("You have: " + str(self.xp) + " XP")
        print("Max Health: " + str(self.max_hp))
        print("Fatigue: " + str(self.fatigue))
        print("Strength: " + str(self.strength))
        print("Defence: " + str(self.defence))
        print("Speed: " + str(self.speed))
        print("Intelligence " + str(self.intelligence))
        print()

    def display_player_bar(self):
        current_level = util.calculate_current_level(self.xp)
        required_xp = util.xp_required_for_level(current_level + 1)
        print("LV. " + str(current_level) + " (XP: " + str(self.xp) + "/" + str(round(required_xp)) + ")", end="")

        # print health
        print()
        print("HP: ", end="")
        render.print_bar(self.health, self.max_hp)
        print(" " + str(self.health) + "/" + str(self.max_hp))
        
        # print fatigue
        print("FT: ", end="")
        render.print_bar(self.fatigue, 100)
        print(" " + str(self.fatigue) + "/" + str(100))

class Locations:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return "[{name}]".format(name=self.name)
    
    def print_description(self):
        print()
        print(self.description)
        print()