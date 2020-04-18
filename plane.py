from vehicle import Vehicle

class Plane(Vehicle):
    def __init__(self, fuel, name, color, speed):
        super().__init__(name, color, speed)
        self.fuel = 0

    # def drive(self):
    #     print(f'"The {self.name} flies past. Rummm! Rummm!"')