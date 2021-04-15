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

def getName():
    return sheetName

def libreUpdate(values):

    #tries to open most recent xls file, if not it goes to Template.xls
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
    
    #saves copy to archive
    try:
        wb.save("/home/pi/Desktop/XLS Archive/" + str(date.month) + str(date.year) +".xls")
    except(RuntimeError, FileNotFoundError):
        wb.save("scripts/sheets/" + str(date.month) + str(date.year) + " - TEST" + ".xls")

def csvUpdate():

    
    #wipes csv
    wipe = open('scripts/webpage/data.csv', 'w')
    wipe.write("")
    #opens up xls doc like in libreUpdate()
    date = datetime.date.today()
    try:
        rb =  xlrd.open_workbook("/home/pi/Desktop/XLS Archive/" + str(date.month) + str(date.year) +".xls")    
    except(RuntimeError, FileNotFoundError):
        rb = xlrd.open_workbook("scripts/sheets/Template.xls")
    sheet = rb.sheet_by_index(0)
    csv = open('scripts/webpage/data.csv', 'a')
    i = 0
    try:
        while True:
            currentRow = sheet.row_values(i) #grab current xls row
            counter = 1
            #writes each value into the csv file
            
            for values in currentRow:
                csv.write(str(values))
                #ensures a line break is placed at the end of each row
                print(len(currentRow))
                if counter == (len(currentRow)):
                    csv.write("\n")
                    break
                else:
                    csv.write(",")
                    counter = counter + 1
                    print(counter)
            i = i + 1
    except IndexError:
        pass


libreUpdate([1,2,3,4,5,6,7,8,9,10])
