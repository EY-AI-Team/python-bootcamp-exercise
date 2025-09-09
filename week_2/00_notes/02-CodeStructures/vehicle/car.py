import os
import sys
import logging

from vehicle_parts.engine import engine as engine

#[START] - Class Body
class car:
    #--------------------------------------------------------------------------------------
    # Initialize all variables used in the class
    #--------------------------------------------------------------------------------------
    def __init__(self):
        self.wheel_count = 0;
        self.type = "";
        self.brand = "";
        self.color = "";

        self.engine = engine();
        logging.debug("Initialize Car Object")

    #--------------------------------------------------------------------------------------
    # Methods to set the car and engine properties
    #--------------------------------------------------------------------------------------
    def set_wheel_count(self, wheel_count: int):
        self.wheel_count = wheel_count;

    def set_type(self, type: str):
        self.type = type;

    def set_brand(self, brand: str):
        self.brand = brand;

    def set_color(self, color: str):
        self.color = color;
    
    def set_engine(self, engine: engine):
        self.engine = engine;
    
    def set_engine_cylinder_count(self, cylinder_count: int):
        self.engine.set_cylinder_count(cylinder_count);
    
    def set_engine_type(self, type: str):
        self.engine.set_type(type);
    
    def set_engine_brand(self, brand: str):
        self.engine.set_brand(brand);
    
    def set_engine_horsepower(self, horsepower: int):
        self.engine.set_horsepower(horsepower); 
    
    def set_engine_fuel_type(self, fuel_type: str):
        self.engine.set_fuel_type(fuel_type);

    #--------------------------------------------------------------------------------------
    # Write car details to console
    #--------------------------------------------------------------------------------------
    def display_details(self):
        
        if self.wheel_count == 0:
            raise "Error: Wheel count not set.";
    
        if self.type == "":
            raise "Error: Type not set.";
    
        if self.brand == "":
            raise "Error: Brand not set.";
    
        if self.color == "":
            raise "Error: Color not set.";
    
        print(f"Car Details: Type = {self.type}, Brand = {self.brand}, Color = {self.color}, Wheel Count = {self.wheel_count}");

    #--------------------------------------------------------------------------------------
    # Write engine details to console
    #--------------------------------------------------------------------------------------
    def calculate_mileage(self, distance: float, fuel_used: float) -> float:
        if fuel_used == 0:
            raise "Error: Fuel used cannot be zero.";
        mileage = distance / fuel_used
        return mileage  
    

    #--------------------------------------------------------------------------------------
    # Write engine details to console
    #--------------------------------------------------------------------------------------
    def display_engine(self):
        print(f"Engine Details: Type = {self.engine.get_type()}, Brand = {self.engine.get_brand()}, Cylinder Count = {self.engine.get_cylinder_count()}, Horsepower = {self.engine.get_horsepower()}, Fuel Type = {self.engine.get_fuel_type()}");  

    #--------------------------------------------------------------------------------------
    # Methods
    #--------------------------------------------------------------------------------------
    def get_details(self):
        details = "Car Details: Type =" + self.type + ", Brand = " + self.brand
        return details

#[END] - Class Body