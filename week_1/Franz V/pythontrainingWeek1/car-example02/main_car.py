import sys
import os

os.chdir(sys.path[0])

from car import car
from engine import engine

carA = car()
carA.set_wheel_count(4)
carA.set_type("Sedan")
carA.set_brand("Toyota")
carA.set_color("Red")

engineA = engine()
engineA.set_cylinder_count(4)
engineA.set_type("V4")
engineA.set_brand("Toyota")
engineA.set_horsepower(150)
engineA.set_fuel_type("Gasoline")

carA.set_engine(engineA)


carA.display_details()
carA.display_engine()

# carA.set_engine_cylinder_count(4)
# carA.set_engine_type("V4")  
# carA.set_engine_brand("Toyota")
# carA.set_engine_horsepower(150)
# carA.set_engine_fuel_type("Gasoline")

carB = car()
carB.set_wheel_count(2)
carB.set_type("Motorcycle")
carB.set_brand("Harley-Davidson")
carB.set_color("Black")


engineB = engine()


engineB.set_cylinder_count(2)
engineB.set_type("V2")
engineB.set_brand("Harley-Davidson")
engineB.set_horsepower(70)
engineB.set_fuel_type("Gasoline")
carB.set_engine(engineB)


carB.display_details()
carB.display_engine()

# carB.set_engine_cylinder_count(2)
# carB.set_engine_type("V2")
# carB.set_engine_brand("Harley-Davidson")
# carB.set_engine_horsepower(70)
# carB.set_engine_fuel_type("Gasoline")


try:


    print("-----")


except Exception as e:
    print(f"An error occurred: {e}")    



