"""
Problem: OOP Practice with Inheritance and Polymorphism

Task:
1. Create a base class `Vehicle` with attributes like brand and model.
   - Add a `__str__` method to display vehicle details.
   - Add a method `start_engine()`.

2. Create a derived class `Car` that inherits from `Vehicle`.
   - Add attributes for number of doors and fuel type.
   - Override the `start_engine()` method with a specific message.

3. Create another derived class `ElectricCar` from `Vehicle`.
   - Add attributes for battery_capacity.
   - Override the `start_engine()` method differently.

4. Demonstrate creating objects of each class and printing their details.

5. Store multiple vehicles (Car, ElectricCar) in a list and
   iterate over them to show polymorphism with `start_engine()`.
"""

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print("Vehicle is started")

    def __str__(self):
        return (
            f"Vehicle brand : {self.brand}\n"
            f"Vehicle model : {self.model}"
        )


class Car(Vehicle):
    def __init__(self, brand, model, doors, fuel_type):
        super().__init__(brand,model)
        self.doors = doors
        self.fuel_type = fuel_type

    def start_engine(self):
        print(f"Normal Car is started")

    def __str__(self):
        return (
            f"{super().__str__()}\n"
            f"Doors : {self.doors}\n"
            f"Fuel type : {self.fuel_type}"
        )


class ElectricCar(Vehicle):
    def __init__(self, brand, model, doors, battery_capacity):
        super().__init__(brand, model)
        self.doors = doors
        self.battery_capacity = battery_capacity

    def start_engine(self):
        print(f"Electric car is started")

    def __str__(self):
        return (
            f"{super().__str__()}\n"
            f"Doors : {self.doors}\n"
            f"Battery Capacity : {self.battery_capacity}"
        )


def main():
    # Create objects of Vehicle, Car, ElectricCar
    # Store them in a list and loop to call start_engine()
    v = Vehicle("Maruti","Maruti800")
    c = Car("Porsche","ZX1", 4,"3km per litre")
    e = ElectricCar("Tesla","XU",4,"5km per hour")

    print(f"Details of Vehicle : {v}\n")
    print(f"Details of Car : {c}\n")
    print(f"Details of Electric Car : {e}\n")


    vehicle_list = [c,e]
    print(f"Engine started by specific vehicle:")
    for vehicle in vehicle_list:
        vehicle.start_engine()

if __name__ == "__main__":
    main()
