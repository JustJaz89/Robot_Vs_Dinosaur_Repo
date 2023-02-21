class Fleet:
    def __init__(self):
        self.robots = ["Megatron", "R2D2", "T_800"]

    def create_fleet(self, robots):
        for robot in robots:
            self.robots.append(robot)