import weapon

class Robot:
    def __init__(self,name):
        self.name = name
        self.health = 100
        self.weapon = "None"

    def attack_dinosaur(self, dinosaur):
        dinosaur.health = dinosaur.health - int(self.weapon.attack_power)
        print(f"{self.name} attacked {dinosaur} with {self.weapon.name} for {self.weapon.attack_power} damage!\n{dinosaur.name}'s health is now {dinosaur.health}")
        if (dinosaur.health <= 0):
            print(f"\n{dinosaur.name} has been killed!")

    def select_weapon(self, weapons: list):
        i = 1
        print("\nAvailable Weapons: ")
        for weapon in weapons:
            print(f"{i + 1}: {weapon.name}")
            i += 1
        selected_weapon = input("Please select a weapon number: ")
        self.weapon = weapons[selected_weapon]
        self.weapon.is_equipped = True
        print(f"{weapon} selected")