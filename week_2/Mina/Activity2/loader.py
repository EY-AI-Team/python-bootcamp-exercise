def load_csv_with_validation(file_path, validate_row):
    """
    Loads a CSV file, validates each row, and returns (header, valid_rows, errors).
    """
    valid_rows = []
    errors = []
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    if not lines:
        raise Exception("File is empty.")
    header = lines[0].strip().split(',')
    for i, line in enumerate(lines[1:], start=2):
        row = line.strip().split(',')
        row_errors = validate_row(row)
        if row_errors:
            errors.append((i, row, row_errors))
        else:
            valid_rows.append(row)
    return header, valid_rows, errors

