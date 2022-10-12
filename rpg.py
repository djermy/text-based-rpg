class Player:
    max_hp = 100
    def __init__(self, name, gender, max_hp, health, fatigue, defence, strength, speed, intelligence):
        self.name = name
        self.gender = gender
        self.max_hp = max_hp
        self.health = health
        self.fatigue = fatigue
        self.defence = defence
        self.strength = strength
        self.speed = speed
        self.intelligence = intelligence

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