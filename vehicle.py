class Vehicle:
    def __init__(self, name, color, speed):
        super().__init__()
        self.name = name
        self.color = color
        self.speed = speed

    def drive(self):
        print("We're moving!")