from vehicle import Vehicle

class Plane(Vehicle):
    def __init__(self, fuel, name, color, speed):
        super().__init__(name, color, speed)
        self.fuel = 0

    def drive(self):
        print(f'The {self.name} flies past. Rummm! Rummm!')

    def turn(self, direction):
        print(f'The {self.name} turned {direction}.')

    def stop(self):
        print(f'The {self.color} {self.name} rolls to a stop after rolling a mile down the runway."')