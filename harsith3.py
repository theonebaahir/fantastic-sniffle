class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def display_info(self):
        print(f"Vehicle Name: {self.name}")
        print(f"Mileage: {self.mileage} km/l")
        print(f"Capacity: {self.capacity} passengers")

class Bus(Vehicle):
    def calculate_fare(self):
        # Simple fare calculation: Rs. 100 per passenger
        fare_per_passenger = 100
        total_fare = self.capacity * fare_per_passenger
        return total_fare

# Create a Bus object
school_bus = Bus("School Volvo", 8, 50)

# Display vehicle info
school_bus.display_info()

# Display fare
print("Total Fare: ₹", school_bus.calculate_fare())
