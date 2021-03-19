#!/usr/bin/python
import gspread as gspread
from oauth2client.service_account import ServiceAccountCredentials
import xlwt as xlwt

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('scripts/quickstart-1614790577278-273c4a82a923.json', scope)

client = gspread.authorize(creds)

def SheetUpdate(sheetName, values):
    sheet = client.open(sheetName)
    sheetInstance = sheet.get_worksheet(0)
    sheetInstance.append_row(values)

def libreUpdate():
    wb = xlwt.open_workbook
    ws = wb.append_row()