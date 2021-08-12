import glob
import openpyxl
from openpyxl import load_workbook
from openpyxl.drawing import image
import os
sf = StyleFrame(df)

sf.set_column_width_dict(col_width_dict={
    ("OOO"): 25.5,
    ("XXXX", "JJJJ", "XXXXX", "BBBB", "ZZZZZ") : 20,
    ("TTTTT"): 65.5
 })

all_rows = sf.row_indexes
sf.set_row_height_dict(row_height_dict={
    all_rows[1:]: 120
})

sf.to_excel('1.xlsx',
            sheet_name='Sheet1', #Create sheet
            right_to_left=False,
            columns_and_rows_to_freeze='A1',
            row_to_add_filters=0).save()


col = 0
wb = load_workbook('1.xlsx')
ws = wb.worksheets[0]

searchedfiles = sorted(glob.glob("tablelog/*.jpg"), key=os.path.getmtime)
for fn in searchedfiles :
    img = openpyxl.drawing.image.Image(fn) # create image instances
    c = str(col + 2)
    ws.add_image(img, 'A' + c)
    col = col + 1
wb.save('1.xlsx')