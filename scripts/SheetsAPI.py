#!/usr/bin/python
import gspread 
from oauth2client.service_account import ServiceAccountCredentials
from xlutils.copy import copy
import xlwt
import xlrd as xlrd

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('scripts/quickstart-1614790577278-273c4a82a923.json', scope)

client = gspread.authorize(creds)

def SheetUpdate(sheetName, values):
    sheet = client.open(sheetName)
    sheetInstance = sheet.get_worksheet(0)
    sheetInstance.append_row(values)
    libreUpdate(sheetName, values)



def libreUpdate(sheetName, values):

    rb =  xlrd.open_workbook("scripts/TestSheet.xls")
    sheet = rb.sheet_by_index(0)

    rowCount = sheet.nrows
    for i in range(rowCount) :
        emptyRow = 0
        if(sheet.cell_value(i, 0) == ""):
            emptyRow = i

 

    wb = copy(rb)
    sheet = wb.get_sheet(0)



    sheet.write(emptyRow,0, "test")
    sheet.write(5, 5, 'TestSheet 2')
  
    wb.save("scripts/TestSheet.xls")

libreUpdate('test',1)