#!/usr/bin/python
import time 
import Timer 
# Dictionary assigning every employee to a card number
employeeNames = {3194967166 : "Emmanuel",1128644206 : "Sayeh",3201638574 : "Samantha",3194936622 : "Terri",3193054270 : "Marina",1132207246 : "Chue",1132849950 : "Timothy",52632090 : "Khandaker",1073433162 : "Michael",3186384958 : "Edin",3186356286 : "Derrick",3185943598 : "Eduardo",3185992142 : "Gordon",3186706382 : "Bryan",3185911774 : "Myron",3187063006 : "Jonathon",3186258206 : "Samsodin",3186236478 : "Oudom",3186648926 : "Candice",1225119082 : "Kevin",1232589594 : "Sara",1225917706 : "Asaf",1225048442 : "Wendy",1225976746 : "Paul",1225314026 : "Miguel",1225347642 : "Walfri",1230014186 : "Ernesto",1225445258 : "Charles",1225124458 : "Monique",2103732382 : "Randy",3331579884 : "Raul",2102780110 : "David",2103861214 : "Alessandro",2102692382 : "Thelma",2103924478 : "Mark",2103838382 : "Cao",2103224910 : "William",2103835326 : "Ben"}

# Determines if someone different clocked in when someone else is clocked in and returns the name of the employee who didnt clock out and the time since they clocked in.
def differentEmployee(elapsedTime, worker1, worker2):
  formattedTime = Timer.formatTime(elapsedTime)
  return("\n" + worker1 + " forgot to clock out and " + worker2 + " clocked in after " + formattedTime)

# If a new employee swipes their card, it will stop the current employee's timer and begin one for the new employee.
def employeeOverride(oldEmployee, newEmployee, startTime):
  firstScan = oldEmployee
  elapsedTime = time.time() - startTime
  formattedTime = Timer.formatTime(elapsedTime)
  startTime = Timer.beginTime()
  print ("\n" + oldEmployee + " worked for " + formattedTime + " before " + newEmployee + " clocked in. " + newEmployee + " is now clocked in. Scan their card to end the timer.\n")
  firstScan = newEmployee
  secondScan = employeeNames[int(raw_input("\nScan again to stop\n"))]
  elapsedTime = Timer.finishTime(startTime)

  if(not firstScan == secondScan):
    employeeOverride(firstScan, secondScan, startTime)
  else:
    return(Timer.formatTimeWithWorker(elapsedTime, firstScan))
