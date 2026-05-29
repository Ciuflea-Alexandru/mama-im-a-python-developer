# Define a series of classes that represent multiple vehicles

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"Vehicle: {self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def drive(self):
        return f"The {self.brand} {self.model} is driving with {self.doors} doors."

class Motorcycle(Vehicle):
    def wheelie(self):
        return f"The {self.brand} {self.model} is doing a wheelie!"


my_car = Car("Toyota", "Camry", 4)
my_bike = Motorcycle("Harley-Davidson", "Street 750")

print(my_car.display_info())
print(my_car.drive())
print("-" * 20)
print(my_bike.display_info())
print(my_bike.wheelie())