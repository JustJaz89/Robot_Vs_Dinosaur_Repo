import weapon

class Robot:
    def __init__(self,name):
        self.name = name
        self.health = 100
        self.weapon = weapon.Weapon("Pistol", )

    def attack(self, dinosaur):
        print(f"{self.name} attacked {dinosaur}")