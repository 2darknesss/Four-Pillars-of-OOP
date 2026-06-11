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

for vehicle in vehicles:
    print(vehicle.show_information())