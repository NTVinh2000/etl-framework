import openpyxl

wb = openpyxl.load_workbook(filename=xl_path)

for i in wb.worksheets:
    if i.sheet_state == "visible":
        print(sheet_name)
#do what you need to...
#%%
