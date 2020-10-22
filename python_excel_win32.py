import os
import win32com.client


xlApp = win32com.client.Dispatch("Excel.Application")
xlApp.Visible = True


# Open the file we want in Excel
root = os.getcwd()
file1 = os.path.join(root, 'theo_doi_tinh_trang_don.xlsx')
file2 = os.path.join(root, 'Thong ke tinh trang don.xlsx')
workbook1 = xlApp.Workbooks.Open(file1)
workbook2 = xlApp.Workbooks.Open(file2)

# Select Sheet
ws1 = workbook1.Sheets(1) # Index from 1 to end
ws1 = workbook1.Sheets('Data') # Select by name

# Select Range
Range1 = ws1.Range("A1:A10")
# Select Cell
Cell1 = ws1.Range('A1')
Cell1 = ws1.Cells(1, 2) # Row-Column




# Close and Save
# workbook1.Close(True)
workbook2.Close(True)