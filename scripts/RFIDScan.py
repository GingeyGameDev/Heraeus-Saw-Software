#!/usr/bin/python
import time 
import Timer 
from main import setRunning

# Dictionary assigning every employee to a card number
employeeNames = {3194967166 : "Emmanuel",1128644206 : "Sayeh",3201638574 : "Samantha",3194936622 : "Terri",3193054270 : "Marina",1132207246 : "Chue",1132849950 : "Timothy",52632090 : "Khandaker",1073433162 : "Michael",3186384958 : "Edin",3186356286 : "Derrick",3185943598 : "Eduardo",3185992142 : "Gordon",3186706382 : "Bryan",3185911774 : "Myron",3187063006 : "Jonathon",3186258206 : "Samsodin",3186236478 : "Oudom",3186648926 : "Candice",1225119082 : "Kevin",1232589594 : "Sara",1225917706 : "Asaf",1225048442 : "Wendy",1225976746 : "Paul",1225314026 : "Miguel",1225347642 : "Walfri",1230014186 : "Ernesto",1225445258 : "Charles",1225124458 : "Monique",2103732382 : "Randy",3331579884 : "Raul",2102780110 : "David",2103861214 : "Alessandro",2102692382 : "Thelma",2103924478 : "Mark",2103838382 : "Cao",2103224910 : "William",2103835326 : "Ben"}

# Determines if someone different clocked in when someone else is clocked in and returns the name of the employee who didnt clock out and the time since they clocked in.
def differentEmployee(elapsedTime, worker1, worker2):
  formattedTime = Timer.formatTime(elapsedTime)
  return("\n" + worker1 + " forgot to clock out and " + worker2 + " clocked in after " + formattedTime)

# If a new employee swipes their card, it will stop the current employee's timer and begin one for the new employee.
"""def employeeOverride(oldEmployee, newEmployee, startTime):
  firstScan = oldEmployee
  timeAndWorker = [oldEmployee]
  firstElapsedTime = Timer.finishTime(startTime)
  timeAndWorker.append(firstElapsedTime)
  startTime = Timer.beginTime()
  firstScan = newEmployee
  secondScan = employeeNames[int(input("\nScan again to stop\n"))]
  elapsedTime = Timer.finishTime(startTime)
  timeAndWorker.append(elapsedTime)
  timeAndWorker.append(secondScan)

  if(not firstScan == secondScan):
    print("\n" + timeAndWorker[0] + " worked for " + str(timeAndWorker[1]) + " before " + timeAndWorker[3] + " clocked in. They worked for " + str(timeAndWorker[2]) + "\n")
    employeeOverride(firstScan, secondScan, startTime)
  else:
    #ORDER: Name of first employee that clocked in, Elapsed time of first employees shift, Elapsed time of second employee's shift, name of second employee that clocked in.
    print("\n" + timeAndWorker[0] + " worked for " + str(timeAndWorker[1]) + " before " + timeAndWorker[3] + " clocked in. They worked for " + str(timeAndWorkers[2]) + "\n")
    return(timeAndWorker)"""

#am rewriting this so it is more legibile. I just wanna be able to change it and things like that when i need to
def employeeOverride(oldEmployee, newEmployee, startTime):
  firstElapsedTime = Timer.finishTime(startTime)

  print(newEmployee + " has scanned in and scanned " + oldEmployee + " out. " + str(firstElapsedTime) + " has been logged for " + oldEmployee + " and the timer has started for " + newEmployee + ".")

  newStartTime = Timer.beginTime()
  newFirstScan = newEmployee

  newSecondScan = employeeNames[int(input("\nScan again to stop\n"))]

  #WRITE TO SHEET HERE!!!
  setRunning(False)

  if(not newFirstScan == newSecondScan):
    setRunning(True)
    employeeOverride(newEmployee, newSecondScan, newStartTime)