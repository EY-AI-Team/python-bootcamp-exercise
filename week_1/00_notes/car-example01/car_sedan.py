import os
import sys

from car import car

#[START] - Class Body
class car_sedan(car):
    CAR_TYPE = "Sedan"
    #--------------------------------------------------------------------------------------
    # Initialize all variables used in the class
    #--------------------------------------------------------------------------------------
    def __init__(self):
        super().__init__()
        self.door_count = 0;

    #Methods
    def set_door_count(self, door_count: int):
        self.door_count = door_count;

    def display_details(self):
        print(f"Car Details: Type = {self.CAR_TYPE}, Brand = {self.brand}, Color = {self.color}, Wheel Count = {self.wheel_count}");

    #Properties Get
    def get_wheel_count(self):
        return self.wheel_count;
    

#[END] - Class Body