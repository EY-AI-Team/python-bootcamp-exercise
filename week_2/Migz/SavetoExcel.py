import openpyxl 

def process_rows(rows):

    wb = openpyxl.load_workbook("C:\Users\CS158EW\OneDrive - EY\Desktop\Python Training\python-bootcamp-exercise\week_2\Migz\SaveExcel.xlsx") 
    sheet = wb.active 
    for row in rows:
        sheet.append(row)
    wb.save("C:\Users\CS158EW\OneDrive - EY\Desktop\Python Training\python-bootcamp-exercise\week_2\Migz\SaveExcel.xlsx")