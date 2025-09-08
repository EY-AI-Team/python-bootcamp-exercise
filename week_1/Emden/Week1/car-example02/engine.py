import os
import sys

#[START] - Class Body
class engine:
    #--------------------------------------------------------------------------------------
    # Initialize all variables used in the class
    #--------------------------------------------------------------------------------------
    def __init__(self):
        self.cylinder_count = 0;
        self.type = "";
        self.brand = "";
        self.horsepower = 0;
        self.fuel_type = "";
    
    #Methods
    def set_cylinder_count(self, cylinder_count: int):
        self.cylinder_count = cylinder_count;

    #Properties Set
    def set_type(self, type: str):
        self.type = type;

    def set_brand(self, brand: str):
        self.brand = brand;

    def set_horsepower(self, horsepower: int):
        self.horsepower = horsepower;
    
    def set_fuel_type(self, fuel_type: str):
        self.fuel_type = fuel_type;
    
    #Properties Get
    def get_cylinder_count(self):
        return self.cylinder_count;

    def get_type(self):
        return self.type;

    def get_brand(self):
        return self.brand;

    def get_horsepower(self):
        return self.horsepower;

    def get_fuel_type(self):
        return self.fuel_type; 
 


#[END] - Class Body