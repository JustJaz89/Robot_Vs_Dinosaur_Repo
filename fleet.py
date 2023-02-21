class Fleet:
    def __init__(self):
        self.robots = ["megatron", "r2d2", "t_800"]

    def create_fleet(self, robots):
        for robot in robots:
            self.robots.append(robot)