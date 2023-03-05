class Dinosaur:
    def __init__(self, name:int, attack_power: int):
        self.name = name
        self.health = 100
        self.attack_power = attack_power
        self.attacks = ("Claw", "Bite", "Stomp")
        self.attack = ""

    def attack_robot(self, robot):
        self.select_attack()
        robot.health = robot.health - int(self.attack_power)
        print(f"{self.name} attacked {robot.name} with {self.attack} for {self.attack_power} damage!\n{robot.name}'s health is now {robot.health}")
        if (robot.health) <= 0:
            print(f"\n{robot.name} has been destroyed!")

    def select_attack(self):
        print("\nSelect an attack: ")
        i = 1
        for attack in self.attacks:
            print(f"{i}: {attack}")
            i += 1
        self.attack = self.attacks(int(input("\nEnter number: ")))