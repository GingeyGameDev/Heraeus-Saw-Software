import RFIDScan
import time
#!/usr/bin/python

employeeNames = {3194967166 : "Emmanuel",1128644206 : "Sayeh",3201638574 : "Samantha",3194936622 : "Terri",3193054270 : "Marina",1132207246 : "Chue",1132849950 : "Timothy",52632090 : "Khandaker",1073433162 : "Michael",3186384958 : "Edin",3186356286 : "Derrick",3185943598 : "Eduardo",3185992142 : "Gordon",3186706382 : "Bryan",3185911774 : "Myron",3187063006 : "Jonathon",3186258206 : "Samsodin",3186236478 : "Oudom",3186648926 : "Candice",1225119082 : "Kevin",1232589594 : "Sara",1225917706 : "Asaf",1225048442 : "Wendy",1225976746 : "Paul",1225314026 : "Miguel",1225347642 : "Walfri",1230014186 : "Ernesto",1225445258 : "Charles",1225124458 : "Monique",2103732382 : "Randy",3331579884 : "Raul",2102780110 : "David",2103861214 : "Alessandro",2102692382 : "Thelma",2103924478 : "Mark",2103838382 : "Cao",2103224910 : "William",2103835326 : "Ben"}
while True:
  firstScan = employeeNames[int(raw_input("scan\n"))]

  startTime = RFIDScan.beginTime()
  secondScan = employeeNames[int(raw_input("\nScan again to stop\n"))]
  elapsedTime = RFIDScan.finishTime(startTime)

  if(not firstScan == secondScan):
    print RFIDScan.differentEmployee(elapsedTime,firstScan,secondScan)
  else:
    print RFIDScan.getTimeWorked(elapsedTime, firstScan)