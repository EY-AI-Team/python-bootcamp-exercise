import os
import sys
import logging

os.chdir(sys.path[0])

#Import custom objects
from engine import engine

from car import car
from car_sedan import car_sedan
from car_trucks import car_trucks


#Import logging configuration
from logging_config import setup_logging

#Setup logging
setup_logging()

#Initialize list to hold vehicles
vehicles = []

logging.debug("Starting Application")
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

logging.debug(f"Added the item: {c.get_details()}")
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
logging.debug(f"Added the item: {cs.get_details()}")
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

logging.debug(f"Added the item: {ct.get_details()}")


try:
    print("----------------------------------")
    
    for c in vehicles:
        try:
            c.display_details()
            c.display_engine()
        except Exception as e:
            logging.warning(f"Error displaying vehicle details: {e}")    
        print("----------------------------------")

except Exception as e:
    logging.error(f"Error occurred: {e}")  