from vehicle import Vehicle

class HouseBoat(Vehicle):
    def __init__(self, beer, color, name, speed):
        super().__init__(color, name, speed)
        self.beer = beer

    def drive(self):
        print(f'The {self.name} House Boat slowly cruises past. Sputter sputter!')

    def turn(self, direction):
        print(f'The {self.name} turned {direction} to head south on a trip to the Gulf.')

    def stop(self):
        print(f'The {self.name} came to a slow stop to dock at my favorite on water bar.')