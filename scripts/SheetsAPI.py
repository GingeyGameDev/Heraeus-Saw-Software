#!/usr/bin/python
import gspread as gspread
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

    wb = copy(rb)
    sheet = wb.get_sheet(0)

    sheet.write(1,1, "test")
    sheet.write(5, 5, 'TestSheet 2')
    sheet.write_merge(3, 4, 3, 4, 'TestSheet 3'

    wb.save('scripts/TestSheet.xls')

libreUpdate('TestSheet', 1) 