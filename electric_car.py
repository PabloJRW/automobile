from car_main import *

class ElectricCar(Car):

    def __init__(self, brand, model, year, battery_charge):
        super().__init__(brand, model, year)
        self.battery_charge = int(battery_charge)

    
    def describe_battery(self):
        description = f"Battery is {self.battery_charge}% charged"
        return description

my_tesla = ElectricCar('Tesla','Model S', 2022, 97)
print(my_tesla.get_descriptive())
print(my_tesla.describe_battery())