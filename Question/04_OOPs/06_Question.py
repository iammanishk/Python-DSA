# Add a static method to the Car class that returns a general description of a car. 


class Car:

    car_count = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.car_count +=1

    def display_info(self):
        Information = f"The brand of the car is: {self.__brand} and the model is: {self.__model}"
        return Information
    
    def fuel_type(self):
        return "Petrol and Diesel"
    
    @staticmethod
    def generalDescription():
        return "A car is a vehicle that has 4 wheels and runs on fuel"
    
    @property
    def __model(self):
        return self.__model
    

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
# print(f"The brand of my car is: {my_car.brand} and the model is: {my_car.model}")
# print(my_car.fuel_type())

# my_car.model = "Corolla"
print(my_car.__model)

# print(Car.generalDescription())

# myElectricCar = ElectricCar("Tesla", "Model S", 100)
# print(myElectricCar.display_info())
# print(myElectricCar.fuel_type())


# print(Car.car_count)
