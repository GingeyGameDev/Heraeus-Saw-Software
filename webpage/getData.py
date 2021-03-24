#!/usr/bin/python
import gspread
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']


creds = Credentials.from_service_account_file('quickstart-1614790577278-273c4a82a923.json', scopes=scope)
client = gspread.authorize(creds)

sheet = client.open("Test sheet")
sheetInstance = sheet.get_worksheet(0)

#wipes csv file
wipe = open.('data.csv', 'w')
wipe.write("")

i = 0
i = 0
while i < 30:
    currentRow = sheetInstance.row_values(i) 
    csv = open('data.csv', 'a')
    #writes each value into the csv file
    for value in currentRow:
        csv.write(str(currentRow[value - 1]))
        #ensures a line break is placed at the end of each row
        if value == (len(currentRow)):
            csv.write("\n")
            break
        else:
            csv.write(",")
    i = i + 1


