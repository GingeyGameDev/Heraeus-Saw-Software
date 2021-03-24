#!/usr/bin/python
import gspread
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']


creds = Credentials.from_service_account_file('quickstart-1614790577278-273c4a82a923.json', scopes=scope)
client = gspread.authorize(creds)

sheet = client.open("Test sheet")
sheetInstance = sheet.get_worksheet(0)

i = 0
while i < 30:
    currentRow = sheetInstance.row_values(i) 
    for 
