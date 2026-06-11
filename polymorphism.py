# Polymorphism: different objects (Car, Plane, Ship) share the same method name,
# but each class implements it differently, allowing them to be processed in a single loop.
class Car:
    def show_information(self):
        return "Car: Driving on the road."

class Plane:
    def show_information(self):
        return "Plane: Flying in the sky."

class Ship:
    def show_information(self):
        return "Ship: Sailing on the water."

vehicles = [Car(), Plane(), Ship()]

# A single method call in a loop results in different behaviors depending on the object
for vehicle in vehicles:
    print(vehicle.show_information())