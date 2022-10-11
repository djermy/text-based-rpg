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