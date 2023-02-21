class Herd:
    def __init__(self):
        self.dinosaurs = ["t_rex", "raptor", "spino"]

    def create_herd(self, dinosaurs):
        for dinosaur in dinosaurs:
            self.dinosaurs.append(dinosaur)