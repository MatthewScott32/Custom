from vehicle import Vehicle

class Batmobile(Vehicle):
    def __init__(self, rockets, name, color, speed):
        super().__init__(name, color, speed)
        self.rockets = rockets

    def drive(self):
        print(f'"The {self.name} Batmobile drives past. RRrrrrrummbbble!"')