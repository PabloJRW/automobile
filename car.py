class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer_reading = 0

    
    def get_descriptive(self):
        description = f"{self.brand} {self.model} {self.year}"
        return description.title()


    def read_odometer(self):
        """Show the car's mileage"""
        odometer_description = f"{self.odometer_reading} miles on it"
        return odometer_description


    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back
        """
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll the odometer")
        
class Battery:

    def __init__(self, battery_charge=85):
        """Initialize the battery's attributes."""
        self.battery_charge = battery_charge

    def describe_battery(self):
        """Describe the battery."""
        battery_description = f"Battery is {self.battery_charge}% charged"

        return battery_description 

        
class ElectricCar(Car):

    def __init__(self, brand, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(brand, model, year)
        self.battery = Battery()