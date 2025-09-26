from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import csv
import io
import re

app = FastAPI()

def validate_email(email: str) -> bool:
    pattern = r"[^@]+@[^@]+\.[^@]+"
    return re.match(pattern, email) is not None

def validate_phone(phone: str) -> bool:
    pattern = r"^\d{3}-\d{3}-\d{4}$"
    return re.match(pattern, phone) is not None

@app.post("/get_employee")
async def get_employee(file: UploadFile = File(...)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="File must be a CSV")

    content = await file.read()
    try:
        csvfile = io.StringIO(content.decode("utf-8"))
    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="File encoding must be UTF-8")

    reader = csv.reader(csvfile)
    rows = list(reader)

    if len(rows) == 0:
        raise HTTPException(status_code=400, detail="CSV file is empty")

    header = rows[0]
    if len(header) != 12:
        raise HTTPException(status_code=400, detail="CSV header must have exactly 12 columns")

    valid_employees = []
    invalid_rows = []
    errors_log = []

    for idx, row in enumerate(rows[1:], start=2):
        if len(row) != 12:
            errors_log.append(f"Line {idx}: Incorrect number of columns ({len(row)})")
            invalid_rows.append(row)
            continue

        if any(cell.strip() == "" for cell in row):
            errors_log.append(f"Line {idx}: Empty string found in one or more columns")
            invalid_rows.append(row)
            continue

        try:
            employee_id = int(row[0])
        except ValueError:
            errors_log.append(f"Line {idx}: Employee ID not an integer")
            invalid_rows.append(row)
            continue

        if not validate_email(row[2]):
            errors_log.append(f"Line {idx}: Invalid email format")
            invalid_rows.append(row)
            continue

        if not validate_phone(row[3]):
            errors_log.append(f"Line {idx}: Invalid phone number format")
            invalid_rows.append(row)
            continue

        valid_employees.append(row)

    return JSONResponse(content={
        "valid_employees": valid_employees,
        "invalid_count": len(invalid_rows),
        "errors_log": errors_log
    })
