from vehicle import Vehicle

class Aston(Vehicle):
    def __init__(self, ammo, name, color, speed):
        super().__init__(name, color, speed)
        self.ammo = ammo

    def drive(self):
        print(f'"The {self.name} drives past. RRrrrrrummbbble!"')