import sys
import os

os.chdir(sys.path[0])

from car import car
from car_sedan import car_sedan
from car_trucks import car_trucks
from engine import engine

vehicles = []

#####################################
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
vehicles.append(c)
#####################################
#####################################
cs = car_sedan()
cs.set_wheel_count(2)
cs.set_brand("Honda")
cs.set_color("Black")
cs.set_door_count(2)
cs.set_hybrid(True)

e = engine()
e.set_cylinder_count(2)
e.set_type("V8")
e.set_brand("Honda")
e.set_horsepower(70)
e.set_fuel_type("Gasoline")

cs.set_engine(e)
vehicles.append(cs)
#####################################
#####################################
ct = car_trucks()
ct.set_wheel_count(2)

ct.set_brand("Isuzu")
ct.set_color("Polar White")

e = engine()
e.set_cylinder_count(2)
e.set_type("V16")
e.set_brand("Isuzu")
e.set_horsepower(70)
e.set_fuel_type("Diesel")

ct.set_engine(e)
vehicles.append(ct)

try:
    print("----------------------------------")
    for c in vehicles:
        c.display_details()
        c.display_engine()
        print("----------------------------------")

except Exception as e:
    print(f"An error occurred: {e}")    



