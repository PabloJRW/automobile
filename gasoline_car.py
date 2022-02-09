from car_main import *

class GasCar(Car):

    def __init__(self, brand, model, year, tank_level):
        super().__init__(brand, model, year)
        self.tank_level = int(tank_level)

    
    def describe_tank_level(self):
        tank_description = f"Tank level is {self.tank_level}% of capacity."
        return tank_description

my_carrito = GasCar('nissan','almera','2022', 67)
print(my_carrito.get_descriptive())
print(my_carrito.describe_tank_level())