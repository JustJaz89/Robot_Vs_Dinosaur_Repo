import fleet
import herd
import robot
import dinosaur
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

        gaming = True
        while(gaming == True):
            # self.battle()
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

        megatron = robot.Robot("Megatron")
        r2d2 = robot.Robot("R2D2")
        t_800 = robot.Robot("T-800")

        t_rex = dinosaur.Dinosaur("T-Rex", 50)
        raptor = dinosaur.Dinosaur("Raptor", 25)
        spino = dinosaur.Dinosaur("Spino", 10)

        self.fleet.create_fleet([megatron, r2d2, t_800])
        self.herd.create_herd([t_rex, raptor, spino])

    # def select_game_type(self):
    #     game_type_message = "\nSelect game type: \n1: Single Player\n2: Two Players\n\n#: "
    #     game_type = int(input(game_type_message))
    #     self.use = True if game_type == 1 else False

    def select_teams(self):
        self.p1_selection = "\nSelect your team: \n1: Robots\n2: Dinosaurs\n\n#: "
        if self.p1_selection == "1":
            self.p1_team = "Robots"
            self.p2_team = "Dinosaurs"
        else:
            self.p1_team = "Dinosaurs"
            self.p2_team = "Robots"

    def display_welcome(self):
        print("Welcome to Robots Vs Dinosaurs!\nThere can only be one team left victorious!\n")
        for robot in self.fleet.robots:
            print(f"Robot: {robot.name}")
        for dinosaur in self.herd.dinosaurs:
            print(f"Dinosaur: {dinosaur.name}")
