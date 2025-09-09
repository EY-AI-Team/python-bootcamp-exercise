import sys
import os

os.chdir(sys.path[0])

from car import car
# from sap_login import sap_login

# login = sap_login()
# login.login("admin", "password")
# if login.is_logged_in():
#     print("User has logged in")
# else:
#     print("User has not logged in")
#     login.logout()


carA = car()
carA.set_wheel_count(4)
carA.cartype("Sedan")
carA.set_brand("Toyota")
carA.set_color("Red")

try:
    result = carA.display_details()
    
except Exception as e:
    print(f"An error occurred: {e}")    



