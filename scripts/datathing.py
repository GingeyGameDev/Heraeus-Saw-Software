import xlrd as xlrd
import datetime

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