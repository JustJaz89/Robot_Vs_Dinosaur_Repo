class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = attack_power
        self.attack_type = ("Claw", "Bite", "Stomp")
        self.attack = ""

    def attack(self, robot):
        self.select_attack()
        robot.health = robot.health - int(self.attack_power)
        print(f"\n{self.name} attacked {robot.name} with {self.attack} for {self.attack_power} damage!\n{robot.name}'s health is now {robot.health}")
        if (robot.health(self)):
            print("\nSelect an attack: ")
            i = 1
            for attack in self.attacks:
                print(f"{i}: {attack}")
                i += 1
            self.attack = self.attacks[int(input("\nEnter number: ")) - 1]