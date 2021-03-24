import Timer
import RFIDScan
import SheetsAPI

#dictionary of employees names and RFID codes
employeeNames = {3194967166 : "Emmanuel",1128644206 : "Sayeh",3201638574 : "Samantha",3194936622 : "Terri",3193054270 : "Marina",1132207246 : "Chue",1132849950 : "Timothy",52632090 : "Khandaker",1073433162 : "Michael",3186384958 : "Edin",3186356286 : "Derrick",3185943598 : "Eduardo",3185992142 : "Gordon",3186706382 : "Bryan",3185911774 : "Myron",3187063006 : "Jonathon",3186258206 : "Samsodin",3186236478 : "Oudom",3186648926 : "Candice",1225119082 : "Kevin",1232589594 : "Sara",1225917706 : "Asaf",1225048442 : "Wendy",1225976746 : "Paul",1225314026 : "Miguel",1225347642 : "Walfri",1230014186 : "Ernesto",1225445258 : "Charles",1225124458 : "Monique",2103732382 : "Randy",3331579884 : "Raul",2102780110 : "David",2103861214 : "Alessandro",2102692382 : "Thelma",2103924478 : "Mark",2103838382 : "Cao",2103224910 : "William",2103835326 : "Ben"}

#List of RFID codes that won't throw errors
RFIDCodes = [3194967166,1128644206,3201638574,3194936622,3193054270,1132207246,1132849950,52632090,1073433162,3186384958,3186356286,3185943598,3185992142,3186706382,3185911774,3187063006,3186258206,3186236478,3186648926,1225119082,1232589594,1225917706,1225048442,1225976746,1225314026,1225347642,1230014186,1225445258,1225124458,2103732382,3331579884,2102780110,2103861214,2102692382,2103924478,2103838382,2103224910,2103835326]

#Finds if there is a given key in a given array
def find(key, arr):
  for i in arr:
    if i == key:
      return True
  return False

while True:
    while True:
        employeeNum = int(input("Please scan card: \n"))
        if find(employeeNum, RFIDCodes):
            firstScan = employeeNames[employeeNum]
            startTime = Timer.beginTime()
            break
        else:
            print("\nName is not in the database. Please scan again.\n")
    
    while True:
        employeeNum = int(input("\nPlease scan again to exit\n"))
        if find(employeeNum, RFIDCodes):
            secondScan = employeeNames[employeeNum]
            break
        else:
            print("\nName is not in the database. Please scan again\n")

    if not firstScan == secondScan:
        timesAndWorker = RFIDScan.employeeOverride(firstScan, secondScan, startTime)
    else:
        SheetsAPI.SheetUpdate()#put things for the update in here please matt :)
        