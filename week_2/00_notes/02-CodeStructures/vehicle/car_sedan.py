import os
import sys
import warnings

from vehicle.car import car

#[START] - Class Body
class car_sedan(car):
    CAR_TYPE = "Sedan"
    #--------------------------------------------------------------------------------------
    # Initialize all variables used in the class
    #--------------------------------------------------------------------------------------
    def __init__(self):
        super().__init__()
        self.door_count = 0;
        self.type = self.CAR_TYPE;
        self.hybrid = False;

    #Methods
    def set_door_count(self, door_count: int):
        self.door_count = door_count;

    def set_hybrid(self, hybrid: bool):
        self.hybrid = hybrid;
    
    
    def display_details(self):
        print(f"Car Details: Type = {self.type}, Brand = {self.brand}, Color = {self.color}, Wheel Count = {self.wheel_count}");
        print(f"Door Count = {self.door_count}");
        if self.hybrid:
            print("This car is a hybrid vehicle.")
        else:
            print("This car is not a hybrid vehicle.")

    def set_type(self, type):
        warnings.warn(
            "set_type() is deprecated, The type is already initated on the class.",
            DeprecationWarning,
            stacklevel=2
        )


    #Properties Get
    def get_wheel_count(self):
        return self.wheel_count;
    

#[END] - Class Body