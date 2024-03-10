# Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size. 


class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        Information = f"The brand of the car is: {self.brand} and the model is: {self.model}"
        return Information
    

class ElectricCar(Car):

    def __init__(self,brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def display_info(self):
        Information = f"The brand of the car is: {self.brand} and the model is: {self.model} and the battery size is: {self.battery_size}"
        return Information
    

my_car = Car("Toyota", "Supra")
print(f"The brand of my car is: {my_car.brand} and the model is: {my_car.model}")

myElectricCar = ElectricCar("Tesla", "Model S", 100)
print(myElectricCar.display_info())
