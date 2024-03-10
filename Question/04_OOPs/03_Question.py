# Create a Car class with attributes like brand and model. Then create an instance of this class. And add a method to the Car class that displays the full name of the car (brand and model). 

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"The brand of the car is: {self.brand} and the model is: {self.model}")
        
        

    
my_car = Car("Toyota", "Supra")
print(f"The brand of my car is: {my_car.brand} and the model is: {my_car.model}")


info = my_car.display_info()  # method calling
