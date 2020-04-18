from vehicle import Vehicle

class HouseBoat(Vehicle):
    def __init__(self, beer, color, name, speed):
        super().__init__(color, name, speed)
        self.beer = beer

    def drive(self):
        print(f'"The {self.name} House Boat slowly cruises past. Sputter sputter!"')