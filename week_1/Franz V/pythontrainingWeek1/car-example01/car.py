import os
import sys

#[START] - Class Body
class car:
    #--------------------------------------------------------------------------------------
    # Initialize all variables used in the class
    #--------------------------------------------------------------------------------------
    def __init__(self):
        self.wheel_count = 0;
        self.car_type = "";
        self.brand = "";
        self.color = "";

    #Methods
    def set_wheel_count(self, wheel_count: int):
        self.wheel_count = wheel_count;

    def cartype(self, argtype: str):
        car_type = "";
        car_type = argtype;

    def set_brand(self, brand: str):
        self.brand = brand;

    def set_color(self, color: str):
        self.color = color;

    def display_details(self):
        
        if self.wheel_count == 0:
            raise "Error: Wheel count not set.";
    
        if self.car_type == "":
            raise "Error: Type not set.";
    
        if self.brand == "":
            raise "Error: Brand not set.";
    
        if self.color == "":
            raise "Error: Color not set.";
    
        print(f"Car Details: Type = {self.car_type}, Brand = {self.brand}, Color = {self.color}, Wheel Count = {self.wheel_count}");

    

#[END] - Class Body