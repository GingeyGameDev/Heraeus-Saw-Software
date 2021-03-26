#!/usr/bin/python
import gspread 
from oauth2client.service_account import ServiceAccountCredentials
from xlutils.copy import copy
import xlwt
import xlrd as xlrd
import datetime


scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('scripts/quickstart-1614790577278-273c4a82a923.json', scope)

client = gspread.authorize(creds)

def SheetUpdate(sheetName, values):
    sheet = client.open(sheetName)
    sheetInstance = sheet.get_worksheet(0)
    sheetInstance.append_row(values)
    libreUpdate(values)

def libreUpdate(values):

    date = datetime.date.today()
    try:
        rb =  xlrd.open_workbook("/home/pi/Desktop/XLS Archive/" + str(date.month) + str(date.year) +".xls")    
    except(RuntimeError, FileNotFoundError):
        rb = xlrd.open_workbook("scripts/sheets/Template.xls")
        

    sheet = rb.sheet_by_index(0)
    emptyRow = sheet.nrows
    
    wb = copy(rb)
    sheet = wb.get_sheet(0)
    
    
    for ii in range(0, 10):
        for j in range(0,len(values)):
            sheet.write(emptyRow + ii, j, values[j])
  
    try:
        wb.save("/home/pi/Desktop/XLS Archive/" + str(date.month) + str(date.year) +".xls")
    except(RuntimeError, FileNotFoundError):
        wb.save("scripts/sheets/" + str(date.month) + str(date.year) + " - TEST" + ".xls")

libreUpdate([1,2,3,4,5,6,7,8,9,10])
