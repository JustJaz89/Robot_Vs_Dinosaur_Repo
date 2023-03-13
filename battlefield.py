import random
from fleet import Fleet
from herd import Herd
from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.setup()
        self.display_welcome()
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
        pistol = Weapon("Pistol", 10)
        laser_rifle = Weapon("Laser Rifle", 50)
        sword = Weapon("Sword", 25)
        self.weapons = [pistol, laser_rifle, sword]

        megatron = Robot("Megatron")
        r2d2 = Robot("R2D2")
        t_800 = Robot("T-800")

        t_rex = Dinosaur("T-Rex", 50)
        raptor = Dinosaur("Raptor", 25)
        spino = Dinosaur("Spino", 10)

        self.fleet.create_fleet([megatron, r2d2, t_800])
        self.herd.create_herd([t_rex, raptor, spino])

    def select_teams(self):
        self.choose_team = "\nSelect your team: \n1: Robots\n2: Dinosaurs\n\n1 or 2: "
        choose_team = int(input(self.choose_team))
        if choose_team == 1:
            print("You have selected the fleet of Robots!")
            return choose_team
        elif choose_team == 2:
            print("You have selected the herd of Dinosaurs!")
            return choose_team
        else:
            print("Invalid answer. Try again. ")

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
            self.robot_turn(robot)
        for dinosaur in self.herd.dinosaurs:
            self.dinosaur_turn(dinosaur)

    def robot_turn(self, robot):
        if len(self.herd.dinosaurs) > 0:
            print(f"\nIt's {robot.name}'s turn.")
            action = int(input("\nSelect an action:\n1. Change weapon\n2: Attack\nEnter #: "))
            if action == 1:
                robot.select_weapon(self.weapons)
            self.show_dinosaur_opponent_options()
            target = int(input("\nChoose target #: ")) - 1
            dinosaur = self.herd.dinosaurs(target)
            robot.attack_dinosaur(dinosaur)
            if dinosaur.hp <= 0:
                self.herd.dinosaurs.remove(dinosaur)
            input("Continue...")

    def dinosaur_turn(self, dinosaur):
        if len(self.fleet.robots) > 0:
            print(f"\nIt's {dinosaur.name}'s turn.")
            self.show_robot_opponent_options()
            target = int(input("\nChoose target #: ")) - 1
            robot = self.fleet.robots(target)
            dinosaur.attack_robot(robot)
            if robot.hp <= 0:
                self.fleet.robots.remove(robot)
            input("Continue...")

    def show_robot_opponent_options(self):
        print("\nThese are the available opponents to attack: ")
        i = 1
        for robot in self.fleet.robots:
            print(f"{i}: {robot.name}")
            i += 1

    def show_dinosaur_opponent_options(self):
        print("\nThese are the available opponents to attack: ")
        i = 1
        for dinosaur in self.herd.dinosaurs:
            print(f"{i}: {dinosaur.name}")
            i += 1

    
        # first_turn = random.randint(1, 2)
        # if first_turn == 1:
        #     print("Robots are up first...")
        #     first_turn = 1
        # elif first_turn == 2:
        #     print("Dinosaurs are up first...")
        #     first_turn = 2
        # elif first_turn == 1:
        #     while len


    # def attack_dinosaur(self, dinosaur):
    #     dinosaur.health = dinosaur.health - int(self.weapons.attack_power)
    #     print(f"{self.name} attacked {dinosaur} with {self.weapon.name} for {self.weapon.attack_power} damage!\n{dinosaur.name}'s health is now {dinosaur.health}")
    #     if (dinosaur.health <= 0):
    #         print(f"\n{dinosaur.name} has been killed!")

    def display_winner(self, winner):
        if winner == "Robots":
            print("Robots WIN!")
        else:
            print("Dinosaurs WIN!")
