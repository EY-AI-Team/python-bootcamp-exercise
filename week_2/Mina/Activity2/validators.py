def validate_row(row):
    errors = []
    if len(row) != 12:
        errors.append("Row does not have 12 columns.")
    if any(str(cell).strip() == "" for cell in row):
        errors.append("Empty string in one or more columns.")
    try:
        int(row[0])
    except:
        errors.append("Employee ID is not an integer.")
    if "@" not in row[4] or "." not in row[4]:
        errors.append("Invalid email address.")
    if not re.match(r"\d{3}-\d{3}-\d{4}$", row[5]):
        errors.append("Invalid phone number format.")
    return errors