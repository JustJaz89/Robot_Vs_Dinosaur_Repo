import fleet
import herd
from robot import Robot
from dinosaur import Dinosaur
import weapon

class Battlefield:
    def __init__(self):
        self.fleet = fleet.Fleet()
        self.herd = herd.Herd()

    def run_game(self):
        self.setup()
        self.display_welcome()
        # self.select_game_type()
        self.select_teams()
        self.battle_phase()
        self.display_winner()

        gaming = True
        while(gaming == True):
            self.battle_phase()
            if (len(self.herd.dinosaurs) == 0):
                self.display_winners("Robots")
                gaming = False
            elif (len(self.fleet.robots) == 0):
                self.display_winners("Dinosaurs")
                gaming = False

    def setup(self):
        pistol = weapon.Weapon("Pistol", 10)
        laser_rifle = weapon.Weapon("Laser Rifle", 50)
        sword = weapon.Weapon("Sword", 25)
        self.weapons = [pistol, laser_rifle, sword]

        megatron = Robot("Megatron")
        r2d2 = Robot("R2D2")
        t_800 = Robot("T-800")

        t_rex = Dinosaur("T-Rex", 50)
        raptor = Dinosaur("Raptor", 25)
        spino = Dinosaur("Spino", 10)

        self.fleet.create_fleet([megatron, r2d2, t_800])
        self.herd.create_herd([t_rex, raptor, spino])

    # def select_game_type(self):
    #     game_type_message = "\nSelect game type: \n1: Single Player\n2: Two Players\n\n#: "
    #     game_type = int(input(game_type_message))
    #     self.use = True if game_type == 1 else False

    def select_teams(self):
        self.p1_selection = "\nSelect your team: \n1: Robots\n2: Dinosaurs\n\n1 or 2: "
        self.p1_selection = int(input(self.p1_selection))
        if self.p1_selection == "1":
            print("You have selected Robots!")
            # self.p1_team = "Robots"
            # self.ai_team = "Dinosaurs"
        else:
            print("You have selected Dinosaurs!")
            # self.p1_team = "Dinosaurs"
            # self.ai_team = "Robots"

    def display_welcome(self):
        print("Welcome to Robots Vs Dinosaurs!\nThere can only be one team left victorious!\n")
        print("ROBOTS")
        for robot in self.fleet.robots:
            print(f"{robot.name}")
        print("--------")
        print("DINOSAURS")
        for dinosaur in self.herd.dinosaurs:
            print(f"{dinosaur.name}")

    def battle_phase(self):
        for robot in self.fleet.robots:
            self.attack_dinosaur(robot)
        for dinosaur in self.herd.dinosaurs:
            self.attack_robot(dinosaur)

    def attack_dinosaur(self, dinosaur):
        dinosaur.health = dinosaur.health - int(self.weapon.attack_power)
        print(f"{self.name} attacked {dinosaur} with {self.weapon.name} for {self.weapon.attack_power} damage!\n{dinosaur.name}'s health is now {dinosaur.health}")
        if (dinosaur.health <= 0):
            print(f"\n{dinosaur.name} has been killed!")

    def display_winner(self, winner):
        if winner == "Robots":
            print("Robots WIN!")
        else:
            print("Dinosaurs WIN!")
