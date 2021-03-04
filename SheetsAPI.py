#!/usr/bin/python
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('quickstart-1614790577278-273c4a82a923.json', scope)

client = gspread.authorize(creds)

sheet = client.open("Test Sheet")

sheetInstance = sheet.get_worksheet(0)

