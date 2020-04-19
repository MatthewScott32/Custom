from vehicle import Vehicle

class Aston(Vehicle):
    def __init__(self, ammo, name, color, speed):
        super().__init__(name, color, speed)
        self.ammo = ammo

    def drive(self):
        print(f'The {self.name} drives past. RRrrrrrummbbble!')

    def turn(self, direction):
        print(f'The {self.name} turned {direction} to avoid the henchman chasing James Bond.')

    def stop(self):
        print(f'The {self.name} came to a screeching stop at the Casino Royale.')