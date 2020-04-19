from vehicle import Vehicle

class Jeep(Vehicle):
    def __init__(self, tow_rope, color, name, speed ):
        super().__init__(color, name, speed)
        self.tow_rope = tow_rope

    def drive(self):
        print(f'The {self.name} Jeep cruises drives past. Vrooom! Vrooom!')

    def turn(self, direction):
        print(f'The {self.name} turned {direction} to climb a giant hill offroad.')

    def stop(self):
        print(f'The {self.name} stopped to use the {self.tow_rope} rope.')