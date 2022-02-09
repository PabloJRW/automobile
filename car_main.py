class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    
    def get_descriptive(self):
        description = f"{self.brand} {self.model} {self.year}"
        return description.title()


