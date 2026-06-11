class Vehicle:
    def __init__(self, brand, capacity):
        self.brand = brand
        self.capacity = capacity

    def start_engine(self):
        return "Engine started"

class Car(Vehicle):
    def __init__(self, brand, capacity, number_of_doors):
        super().__init__(brand, capacity)
        self.number_of_doors = number_of_doors

    def honk(self):
        return "Beep beep!"

my_car = Car("Toyota", 5, 4)
print(my_car.brand)
print(my_car.start_engine())
print(my_car.honk())