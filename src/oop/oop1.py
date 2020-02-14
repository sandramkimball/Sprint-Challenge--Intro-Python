# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. 
# Put a comment noting which class is the base class

class Vehicle:
    pass

# base is Vehicle
class FlightVehicle(Vehicle):
    pass

# base is FlightVehicle
class Airplane(FlightVehicle):
    pass

# base is FlightVehicle
class Starship(FlightVehicle):
    pass

# base is Vehicle
class GroundVehicle(Vehicle):
    pass

# base is GroundVehicle
class Car(GroundVehicle):
    pass

# base is GroundVehicle
class Motorcycle(GroundVehicle):
    pass