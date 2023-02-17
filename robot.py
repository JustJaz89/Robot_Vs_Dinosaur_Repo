from weapon import Weapon

class Robot:
    def __init__(self,name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon

    def attack(self, dinosaur):
        print(f"{self.name} attacked {dinosaur}")