from vehicle import Vehicle

class Batmobile(Vehicle):
    def __init__(self, rockets, name, color, speed):
        super().__init__(name, color, speed)
        self.rockets = rockets

    def drive(self):
        print(f'The {self.name} Batmobile drives past. RRrrrrrummbbble!')

    def turn(self, direction):
        print(f'The {self.name} turned {direction} while chasing the Joker.')

    def stop(self):
        print(f'The {self.name} stopped abruptly at the Ace Chemicals Plant.')