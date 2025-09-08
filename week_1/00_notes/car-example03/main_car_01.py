import sys
import os

os.chdir(sys.path[0])

from car import car
from engine import engine


cars = []

c = car()
c.set_wheel_count(4)
c.set_type("Sedan")
c.set_brand("Toyota")
c.set_color("Red")

e = engine()
e.set_cylinder_count(4)
e.set_type("V4")
e.set_brand("Toyota")
e.set_horsepower(150)
e.set_fuel_type("Gasoline")
c.set_engine(e)

cars.append(c)

c = car()
c.set_wheel_count(2)
c.set_type("Motorcycle")
c.set_brand("Harley-Davidson")
c.set_color("Black")


e = engine()
e.set_cylinder_count(2)
e.set_type("V2")
e.set_brand("Harley-Davidson")
e.set_horsepower(70)
e.set_fuel_type("Gasoline")
c.set_engine(e)

cars.append(c)

try:
    print("----------------------------------")
    for c in cars:
        c.display_details()
        c.display_engine()
        print("----------------------------------")


except Exception as e:
    print(f"An error occurred: {e}")    



