from aston_martin import Aston
from batmobile import Batmobile
from house_boat import HouseBoat
from jeep import Jeep
from plane import Plane
from vehicle import Vehicle

aston = Aston(120, "Aston Marton", "Silver", 99)
print(f'{aston.name} {aston.color} {aston.speed} mph {aston.ammo}')
aston.drive()
aston.turn('right')
aston.stop()

batmobile = Batmobile(10, "Batmobile", "Black", 132)
print(f'{batmobile.name} {batmobile.color} {batmobile.speed} mph {batmobile.rockets}')
batmobile.drive()
batmobile.turn('left')
batmobile.stop()


house_boat = HouseBoat("Bearded Iris Home Style", "House Boat", "White", 15)
print(f'{house_boat.name} {house_boat.color} {house_boat.speed} mph {house_boat.beer}')
house_boat.drive()
house_boat.turn('right')
house_boat.stop()


jeep = Jeep("front tow", "Jeep", "Blue", 25)
print(f'{jeep.name} {jeep.color} {jeep.speed} mph {jeep.tow_rope}')
jeep.drive()
jeep.turn('left')
jeep.stop()


plane = Plane("15", "Plane", "Red", 150)
print(f'{plane.name} {plane.color} {plane.speed} mph {plane.fuel} gallons')
plane.drive()
plane.turn('right')
plane.stop()
