# Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.
# Add a class variable to Car that keeps track of the number of cars created.


class Car:

    car_count = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.car_count +=1

    def display_info(self):
        Information = f"The brand of the car is: {self.brand} and the model is: {self.model}"
        return Information
    
    def fuel_type(self):
        return "Petrol and Diesel"
    

class ElectricCar(Car):

    def __init__(self,brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def display_info(self):
        Information = f"The brand of the car is: {self.brand} and the model is: {self.model} and the battery size is: {self.battery_size}"
        return Information
    
    def fuel_type(self):
        return "Electricity"
    

my_car = Car("Toyota", "Supra")
print(f"The brand of my car is: {my_car.brand} and the model is: {my_car.model}")
print(my_car.fuel_type())

myElectricCar = ElectricCar("Tesla", "Model S", 100)
print(myElectricCar.display_info())
print(myElectricCar.fuel_type())


print(Car.car_count)
