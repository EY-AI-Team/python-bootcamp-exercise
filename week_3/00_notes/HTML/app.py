from flask import Flask, render_template, flash
import requests
import logging
import json
import os

from logging_config import setup_logging

# Configure logging
setup_logging()
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.urandom(12)

# Routes

@app.route('/')
@app.route('/Home')
def home():
    """Home page with welcome message"""
    return render_template('home.html')

@app.route('/GetEmployees')
def get_employees():
    try:
        # employees = employee_api.get_employees()
        response = requests.get('http://localhost:8000/csv/get_employees')
        raw_employees = json.loads(response.text)
        employees = []
        
        for ctr in range(1, len(raw_employees), 1) :
            
            raw_employee = raw_employees[ctr]
            employee = {
                'EmployeeID': raw_employee[0],
                'FirstName': raw_employee[1],
                'LastName': raw_employee[2],
                'EmailAddress': raw_employee[3],
                'JobTitle': raw_employee[4],
                'PrimaryPhone': raw_employee[5],
                'SecondaryPhone': raw_employee[6],
                'AddedBy': raw_employee[7],
                'AddedOn': raw_employee[8],
                'ModifiedBy': raw_employee[9],
                'ModifiedOn': raw_employee[10],
            }
            employees.append(employee)

        return render_template('employees.html', employees=employees)
                
    except Exception as e:
        logger.error(f"Error fetching employee data: {str(e)}", 'error')
        return render_template('employees.html', employees=[])

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html', error_code=404, error_message="Page not found"), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html',
                         error_code=500,
                         error_message="Internal server error"), 500



if __name__ == '__main__':
    print("Employee Management System")
    print("Starting Flask application...")
    
    # Run Flask app
    app.run(
        host='0.0.0.0',
        port=5001,
        debug=True
    )
