import openpyxl
import xlsxwriter
from openpyxl import Workbook
path="Book2.xlsx"
wb = openpyxl.load_workbook(path)
sheet = wb.get_sheet_by_name('Sheet1')
row=2
rows=1
column=1
while(sheet.cell(row,column).value):
    rows=rows+1
chart1.add_series({
    'name':       '=Sheet1!$B$1',
    'categories': '=Sheet1!$A$2:$A$7',
    'values':     '=Sheet1!$B$2:$B$7',
})
chart1.set_title ({'name': 'Results of sample analysis'})
chart1.set_x_axis({'name': 'Test number'})
chart1.set_y_axis({'name': 'Sample length (mm)'})
chart1.set_style(10)
worksheet.insert_chart('E5', chart1, {'x_offset': 25, 'y_offset': 10})
wb.save(path)