
# Create a Bus child class that inherit from the Vehicle class. The default fare charges of any vehicale is seating_capacity*100. If vehicalde is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So the total fare for the bus will become the final amount = total fare = total fare + 10% of the total fare.

class Vehicles:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def get_fare(self):
        fare = self.seating_capacity * 100
        return fare
    

class Bus(Vehicles):

    def __init__(self, seating_capacity):
        super().__init__(seating_capacity)

    def get_fare(self):
        vehicale_fare = super().get_fare()
        mantanance_fare = 0.1 * vehicale_fare
        total_fare = vehicale_fare + mantanance_fare
        return total_fare
    

vehicale1 = Vehicles(50)
print(f"The fare of the vehicale is: {vehicale1.get_fare()}")

bus1 = Bus(50)
print(f"The fare of the bus is: {bus1.get_fare()}")