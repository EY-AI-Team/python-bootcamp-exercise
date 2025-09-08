import os
import sys

#[START] - Class Body
class sap_login:
    #--------------------------------------------------------------------------------------
    # Initialize all variables used in the class
    #--------------------------------------------------------------------------------------
    def __init__(self):
        has_login = False;

    def login(self, username: str, password: str):
        local_variable_password = password;
        if username == "admin" and password == "password":
            self.has_login = True;
            print("Login successful.");
        else:
            raise "Error: Invalid username or password.";

    def checkelement(self):
        self.has_login = False;
        print("Logged out successfully.");

    def elementexist(self):
        self.has_login = False;
        print("Logged out successfully.");

    def logout(self):
        self.has_login = False;
        print("Logged out successfully.");

    def is_logged_in(self):
        return self.has_login;
