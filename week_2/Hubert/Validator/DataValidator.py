import os
import re
import csv
import logging

#[START] - Class Body
class DataValidator:
    #--------------------------------------------------------------------------------------
    # Initialize all variables used in the class
    #--------------------------------------------------------------------------------------
    def __init__(self, items=None, row_num=0):
        logging.debug("Initialize DataValidator Object")
        self.items_raw = items 
        self.row_num = row_num
    #--------------------------------------------------------------------------------------
    # Validate individual data fields
    #--------------------------------------------------------------------------------------
    def IsValid(self):
        flagValidateContent = True
        
        
        try:
            
            #Common Validations
            for ctr in range(len(self.items_raw)):
                if self.is_empty_string(self.items_raw[ctr]) == True:
                    flagValidateContent = False
                    break;

            #Special Validations
            if self.is_valid_integer(self.items_raw[0])== False:
                flagValidateContent = False;
            
            if self.is_valid_email(self.items_raw[3]) == False:
                flagValidateContent = False;
            
            if self.is_valid_phone(self.items_raw[5])== False:
                flagValidateContent = False;
            
            
        
        except Exception as e:
            logging.error(f"Error validating the item row : {self.row_num} : {e}")
            flagValidateContent = False
        
        return flagValidateContent
    
    #--------------------------------------------------------------------------------------
    # Validate individual data fields
    #--------------------------------------------------------------------------------------
    def is_valid_email(self, email):
    # Basic email validation
        flagValid = True
        pattern = r"^[^@]+@[^@]+\.[^@]+$"

        flagValid = re.match(pattern, email) is not None

        if flagValid == False:
            logging.warning(f"Invalid email format on row : {self.row_num} : {email}")

        return flagValid
    
    #--------------------------------------------------------------------------------------
    # Validate individual data fields
    #--------------------------------------------------------------------------------------
    def is_valid_phone(self, phone):
    # Validate phone number in format ###-###-####
        pattern = r"^\d{3}-\d{3}-\d{4}$"
        flagValid = re.match(pattern, phone.strip()) is not None

        if not flagValid:
            logging.warning(f"Invalid phone number format on row : {self.row_num} : {phone}")

        return flagValid
    
    #--------------------------------------------------------------------------------------
    # Validate individual data fields
    #--------------------------------------------------------------------------------------
    def is_valid_integer(self, value):
        # Validate if string can be converted to integer
        try:
            int(value)
            return True
        except ValueError:
            logging.warning(f"Invalid integer value on row : {self.row_num} : {value}")
            return False

    #--------------------------------------------------------------------------------------
    # Check if a string is empty
    #--------------------------------------------------------------------------------------
    def is_empty_string(self, value):
        # Returns True if the string is empty or only whitespace
        if str(value).strip() == "":
            logging.warning(f"Empty string detected on row : {self.row_num} ")
            return True
        return False   
         