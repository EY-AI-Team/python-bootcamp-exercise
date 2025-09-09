Create the an application with the following description:
    1. Create a windows forms application that will load the content of a CSV file into a table
    2. Use a windows open file dialog to select the file to be loaded
    3. Apply the following validation the content of a CSV file line by line 
        - Single line should be 12 columns
        - There should be no empty string on each column
        - Employee ID should be integer
        - Use basic validation on email address
        - Validate the phone number with the format ###-###-#### 
    
        ** Separate the log entry of invalid line
    4. A CSV file should contain a header, hence file with no header will raise exception
    5. Log all errors into the a single execution log
